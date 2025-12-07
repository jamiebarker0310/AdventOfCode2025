import sys
from jinja2 import Environment, FileSystemLoader


def generate_template():
    env = Environment(
        loader=FileSystemLoader("."), trim_blocks=True, lstrip_blocks=True
    )

    day_template = env.get_template("template/files/template_day.py.j2")
    test_template = env.get_template("template/files/template_test.py.j2")

    day = sys.argv[1].zfill(2)

    context = {"day_n": day}

    day_rendered = day_template.render(context)
    test_rendered = test_template.render(context)

    with open(f"aoc/day_{day}.py", "w") as f:
        f.write(day_rendered)

    with open(f"tests/test_day_{day}.py", "w") as f:
        f.write(test_rendered)

    # create input file
    open(f"aoc/inputs/day_{day}.txt", "w").close()

    # create test input file
    open(f"tests/test_inputs/test_day_{day}.txt", "w").close()


if __name__ == "__main__":
    generate_template()
