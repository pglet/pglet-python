import pglet
from pglet import Image


def test_image_add():
    i = Image(
        src="https://www.w3schools.com/css/img_5terre.jpg",
        alt="This is image",
        title="This is title",
        maximize_frame=False,
    )
    assert isinstance(i, pglet.Control)
    assert isinstance(i, pglet.Image)
    assert i.get_cmd_str() == (
        'image alt="This is image" maximizeframe="false" '
        'src="https://www.w3schools.com/css/img_5terre.jpg" title="This is title"'
    ), "Test failed"
