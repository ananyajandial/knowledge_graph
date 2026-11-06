from app.neo4j_service import (
    Neo4jService
)


class GraphLoader:

    def __init__(self):

        self.neo4j = Neo4jService()

    def load_graph(self):

        triples = [

            (
                "Employee",
                "CONTACTS",
                "HR Team"
            ),

            (
                "Employee",
                "USES",
                "HR Portal"
            ),

            (
                "Employee",
                "RECEIVES",
                "Annual Leave"
            ),

            (
                "Engineering Team",
                "FOLLOWS",
                "Coding Standards"
            )
        ]

        with self.neo4j.driver.session() as session:

            for source, relation, target in triples:

                query = f"""
                MERGE (a:Entity {{
                    name: $source
                }})

                MERGE (b:Entity {{
                    name: $target
                }})

                MERGE (a)-[:{relation}]->(b)
                """

                session.run(
                    query,
                    source=source,
                    target=target
                )

        print(
            "Knowledge Graph Loaded Successfully!"
        )

    def close(self):

        self.neo4j.close()