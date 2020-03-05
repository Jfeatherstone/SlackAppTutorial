# This is used to read in environment variables, like the port
import os

# This is used to actually respond to post requests
from http.server import HTTPServer, BaseHTTPRequestHandler

# This is used in constructing our messages to send back to Slack
from io import BytesIO

# We read in the port from the environment variable PORT which is defined by Heroku
# This changes every time the dyno is started, so we can't just set it as a static variable
port = int(os.environ['PORT']) # We also have to cast to int because otherwise it would be a string

# We have to have some way to respond to requests, so we define a custom request handler that extends the based request handler
class HTTPRequestHandler(BaseHTTPRequestHandler):

    # Tell the handler what to do when we receive a post request
    # To define what happens when a GET request is sent, you should define do_GET similarly
    def do_POST(self):
        # We want to read in the information that has been sent to us in the POST request
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        # We send a status code of 200, which means we received the request
        self.send_response(200)
        self.end_headers();

        # Now we want to make the information we just received more manageable so that we can actually read it
        # The body variable we have earlier is encoded, so I'm going to decode it assuming that it is using utf-8 format.
        # If this is not the case, you can change this easily enough
        decodedBody = body.decode('utf-8')

        # Now all of the information that is sent to us is of the form 
        # field1=value1&field2=value2&...
        # So we should split our decoded body up by the '&' symbol to get each field
        separatedBody = decodedBody.split('&')

        # Now we don't know what order the fields are in, so lets organize the information in a map
        # instead of an array. This will allow us to refer to each value by the name of the field,
        # instead of the index of the field

        # This just creates two empty arrays the same length as our number of fields
        keys = ['' for i in range(len(fields))]
        values = ['' for i in range(len(fields))]

        # Now we want to iterate over each field-value pair and split them up by the '=' character
        for i in range(len(fields)):
            keys[i], values[i] = fields[i].split('=')

        # Now put the two together into our new data structure
        fields = dict(zip(keys, values))

        # Feel free to print this out to see what it looks like
        #print(fields)

        # Now lets echo whatever the user sent us back
        # The text (beside the command) is kept in the 'text' field

        # Note that we have to encode the message, just as we had to decode the one we received
        messageToSend = f'You said: "{fields["text"]}!'.encode()

        # Now we are going to create an object that can actually be sent back
        response = BytesIO(messageToSend)

        # Now lets send it back
        self.wfile.write(response.getvalue())

        # All that's all there is to it!
        return

# Now we setup the main method
# This is what actually runs on our server, and will utilize our handler we defined about
if __name__ == "__main__":
    # This is our server object, note that we are telling it to respond to requests by using our
    # handler we made above
    # We don't need to set the address for the server ('') since we won't be sending any requests
    # unprovoked, only responding to things
    # And we use the port that we read in earlier
    httpd = HTTPServer(('', port), HTTPRequestHandler)

    # Lets print out what port we are serving on, since it changes each time
    print(f'Serving on port {port}')

    # And now lets tell our server to startup and server until we tell it to stop
    httpd.serve_forever()
