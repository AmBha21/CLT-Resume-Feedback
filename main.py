import click
from methods.process_text import preprocess_text, load_text
from methods.cosine_similarity import calculate_cosine_similarity
from firebase.firebase_utils import create_account_firebase, sign_in_firebase

@click.group()
def cli():
    pass

@cli.command()
@click.argument("resume_file", type=click.Path(exists=True))
@click.argument("job_application_file", type=click.Path(exists=True))
def measure_cosine(resume_file, job_application_file):
    """Measure the cosine similarity between a user's resume and a job application PDF."""
    resume_text = load_text(resume_file)
    job_application_text = load_text(job_application_file)

    resume_text = preprocess_text(resume_text)
    job_application_text = preprocess_text(job_application_text)

    similarity_score = calculate_cosine_similarity(resume_text, job_application_text)

    print(f"Cosine similarity score: {similarity_score:.4f}")

@cli.command()
@click.option("--email", prompt="Enter email", help="Email address for account creation.")
@click.option("--password", prompt="Enter password", hide_input=True, help="Password for account creation.")
@click.option("--username", prompt="Enter username", help="Username for the account.")
def sign_in(email, password, username):
    """Create a new user account."""
    create_account_firebase(email, password, username)

@cli.command()
@click.option("--email", prompt="Enter email", help="Email address for account creation.")
@click.option("--password", prompt="Enter password", hide_input=True, help="Password for account creation.")
def sign_in(email, password):
    """Sign in to an existing user account."""
    sign_in_firebase(email, password)

if __name__ == "__main__":
    cli()