# Website Toast

Turning websites into toast. Because art.

Special thanks to Matt [@fauxfiction](https://github.com/fauxfiction) for the idea and prototype.

## Using this toaster

Build the docker image

    docker build -t mrjackdavis/toaster-website-toast .

Run the docker image

    docker run --name toaster-website -e S3_ACCESS_KEY="secret" -e S3_SECRET_KEY="secret" -e API_PORT="http://api.toast-it.io" -v $(pwd)/src/:/app/ -d mrjackdavis/toaster-website-toast