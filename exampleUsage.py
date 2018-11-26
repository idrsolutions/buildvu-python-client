from BuildVuClient import BuildVu

buildvu = BuildVu('http://localhost:8080/microservice-example')

try:
    # convert() returns a URL (string) where you can view the converted output.
    outputURL = buildvu.convert('path/to/file.pdf')

    # Alternatively, you can specify a url from which the server will download the file to convert.
    #outputURL = buildvu.convert('http://link.to/filename',
    #                            inputType=BuildVu.DOWNLOAD)

    # You can specify a URL that you want to be updated when the coversion finishes
    #outputURL = buildvu.convert('path/to/file.pdf',
    #                            callbackUrl='http://listener.url')

    # You can also specify a directory to download the converted output to:
    # buildvu.convert('path/to/input.pdf', 'path/to/output/dir')

    if outputURL is not None:
        print("Converted: " + outputURL)
except Exception as error:
    print(error)
