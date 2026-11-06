from app.graph_loader import (
    GraphLoader
)


def main():

    loader = GraphLoader()

    loader.load_graph()

    loader.close()


if __name__ == "__main__":
    main()