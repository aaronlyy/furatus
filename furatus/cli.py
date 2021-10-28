import click
from fig import FIG
from algorithm import rand
from furatus import Furatus

@click.command()
@click.option("--hits", "-h", default=1, help="Number of hits", type=int, show_default=True)
@click.option("--output", "-o", default=".", help="Output path", type=str, show_default=True)
@click.option("--algorithm", "-a", default="random", type=click.Choice(["random"], case_sensitive=False), show_default=True)
@click.option("--minlen", "-s", default=6, help="Minimum length of code", type=int, show_default=True)
@click.option("--maxlen", "-e", default="6", help="Maximum length of code", type=int, show_default=True)
def cli(hits, algorithm, output, minlen, maxlen):
    algorithms = {"random": rand} # define algorithm functions

    # print banner and info
    print(FIG)
    print(f"Searching for {hits} image(s) with algorithm {algorithm}.")
    print(f"Images will be saved to './images'.")

    hit_count = 0
    code_count = 0
    f = Furatus()

    for code in algorithms[algorithm](minlen, maxlen): # for endless generate code
        code_count += 1
        success = f.download(f.build_url(code), output, f"{code}.jpg")

        if success:
            print(f"Hit @ {code}")
            hit_count += 1

        if hit_count == hits: # stop searching if hits is reached
            break

    print(f"\nFinished! {code_count} codes tried.\n")


if __name__ == "__main__":
    cli()