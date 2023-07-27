import click

@click.group()
def cli():
    pass

@cli.command()
@click.argument("resume_file")
def measure_cosine(resume_file):
    print(resume_file)

if __name__ == "__main__":
    cli()