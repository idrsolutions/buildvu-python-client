from BuildVuClient import BuildVu as buildvu

input_path = '/path/to/input.pdf'
output_path = '/path/to/output/dir'

buildvu.setup('http://localhost:8080/buildvu-microservice-example')
success = buildvu.convert(input_path, output_path)

print("Conversion success") if success else print("Conversion failed")
