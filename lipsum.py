# encoding: utf-8

from workflow import web


BASE_URL = "http://lipsum.com/feed/json"


def lipsum(wf, what):
    # Get Query from Alfred
    if wf.args[0]:
        query = wf.args[0]
    else:
        query = 1

    # Generate Params
    params = dict(
        what=what,
        amount=query,
        start='no',
    )

    # Request Lorem Ipsum via lipsum.com
    response = web.get(BASE_URL, params)
    response.raise_for_status()

    # Parse JSON from Response
    result = response.json()

    # Return result to Alfred
    wf.add_item(
        title=result["feed"]["lipsum"],
        subtitle=result["feed"]["generated"],
        arg=result["feed"]["lipsum"],
        valid=True,
    )
    wf.send_feedback()
