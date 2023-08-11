import cgi
from base64 import b64encode, b64decode
import face_recognition

def face_match(face_match, email, image):
    """
    Face match function.

    Args:
        face_match (str): The name of the face to match.
        email (str): The email address of the person whose face is being matched.
        image (str): The base64 encoded image of the face to match.

    Returns:
        bool: True if the face matches, False otherwise.
    """

    data_uri = image
    header, encoded = data_uri.split(",", 1)
    data = b64decode(encoded)

    with open("images/known/{}".format(face_match), "wb") as f:
        f.write(data)

    got_image = face_recognition.load_image_file("images/known/{}".format(face_match))

    existing_face_encoding = face_recognition.face_encodings(got_image)[0]

    # Load a sample picture and learn how to recognize it.
    got_image = face_recognition.load_image_file("images/known/{}".format(face_match))

    # Get face encodings for any people in the picture

    got_face_encoding = face_recognition.face_encodings(got_image)[0]

    # See if the face is a match for the known face(s)

    results = face_recognition.compare_faces([existing_face_encoding], got_face_encoding)

    return results[0] == True

if __name__ == "__main__":
    form = cgi.FieldStorage()

    face_match = form.getvalue("face_match")
    email = form.getvalue("email")
    image = form.getvalue("image")

    is_matched = face_match(face_match, email, image)

    if is_matched:
        print("Content-type: text/html\r\n\r\n")
        print("<html>")
        print("<h1>Face Matched</h1>")
        print("<h2>Welcome to the system</h2>")
        print("<img src='images/known/{}'/>".format(face_match))
        print("<h2>Your Face is Matched</h2>")
    else:
        print("Content-type: text/html\r\n\r\n")
        print("<html>")
        print("<h1>Face Not Matched</h1>")
        print("<h2>Your Face is Not Matched</h2>")
        print("<img src='images/known/{}'/>".format(face_match))
        print("<h2>Your Face is Not Matched</h2>")