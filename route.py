from flask import Flask, request, jsonify

from chart.model import database, Author, Song, Performance
from chart.util import load_chart

application = Flask(__name__)
application.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@application.before_request
def before_request():
    database.connect()


@application.after_request
def after_request(response):
    database.close()
    return response


@application.route('/refresh', methods=['POST'])
def refresh():
    Performance.delete().execute()
    Author.delete().execute()
    Song.delete().execute()

    lines = load_chart()

    for line in lines:
        song = Song.create(position=line['position'], name=line['song'])
        for author in line['authors']:
            author, _ = Author.get_or_create(name=author)
            Performance.create(song=song.id, author=author.id)

    return jsonify(lines), 200


@application.route('/search', methods=['GET'])
def search():
    author = request.args.get('author', None)

    query = (Performance
             .select(Song.position, Song.name.alias('song'))
             .join(Song, on=(Performance.song == Song.id)))

    if author:
        query = (query
                 .join(Author, on=(Performance.author == Author.id))
                 .where(Author.name == author))

    performances = list(query
                        .distinct()
                        .dicts())

    return jsonify(performances), 200
