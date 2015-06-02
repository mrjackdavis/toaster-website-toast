# Website Toast

Turning websites into toast. Because art.

## Using this toaster

Build the docker image

    docker build -t mrjackdavis/toaster-website-toast .

Run the docker image

    docker run --name toaster-website -v $(pwd)/src/:/app/ -d mrjackdavis/toaster-website-toast