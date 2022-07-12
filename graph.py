"""
Quokka Maze
===========

This file represents the quokka maze, a graph of locations where a quokka is
trying to find a new home.

Please help the quokkas find a path from their current home to their
destination such that they have sufficient food along the way!

*** Assignment Notes ***

This is the main file that will be interacted with during testing.
All functions to implement are marked with a `TODO` comment.

Please implement these methods to help the quokkas find their new home!
"""

from typing import List, Union

from vertex import Vertex


class QuokkaMaze:
    """
    Quokka Maze
    -----------

    This class is the undirected graph class that will contain all the
    information about the locations between the Quokka colony's current home
    and their final destination.

    We _will_ be performing some minor adversarial testing this time, so make
    sure you're performing checks and ensuring that the graph is a valid simple
    graph!

    ===== Functions =====

        * block_edge(u, v) - removes the edge between vertex `u` and vertex `v`
        * fix_edge(u, v) - fixes the edge between vertex `u` and `v`. or adds an
            edge if non-existent
        * find_path(s, t, k) - find a SIMPLE path from vertex `s` to vertex `t`
            such that from any location with food along this simple path we
            reach the next location with food in at most `k` steps
        * exists_path_with_extra_food(s, t, k, x) - returns whether it’s
            possible for the quokkas to make it from s to t along a simple path
            where from any location with food we reach the next location with
            food in at most k steps, by placing food at at most x new locations
        * find_location_of_extra_food(s, t, k, x) - returns at most x locations
            where we can add food, such that afterwards there exists a valid
            path from s to t with food at most k steps between each other.
        * minimize_extra_food(s, t, k) - returns the smallest `x` locations,
            such that adding food at these x locations guarantees there exists
            a path from s to t with at most k steps between food.

    ===== Notes ======

    * We _will_ be adversarially testing, so make sure you check your params!
    * The ordering of vertices in the `vertex.edges` does not matter.
    * You MUST check that `k>=0` and `x>=0` for the respective functions
        * find_path (k must be greater than or equal to 0)
        * exists_path_with_extra_food (k and x must be greater than or equal to
            0)
    * This is an undirected graph, so you don't need to worry about the
        direction of traversing during your path finding.
    * This is a SIMPLE GRAPH, your functions should ensure that it stays that
        way.
    * All vertices in the graph SHOULD BE UNIQUE! IT SHOULD NOT BE POSSIBLE
        TO ADD DUPLICATE VERTICES! (i.e the same vertex instance)
    """

    def __init__(self) -> None:
        """
        Initialises an empty graph with a list of empty vertices.
        """
        self.vertices = []

    def add_vertex(self, v: Vertex) -> bool:
        """
        Adds a vertex to the graph.
        Returns whether the operation was successful or not.

        :param v - The vertex to add to the graph.
        :return true if the vertex was correctly added, else false
        """
        # TODO implement me, please?
        pass

    def fix_edge(self, u: Vertex, v: Vertex) -> bool:
        """
        Fixes the edge between two vertices, u and v.
        If an edge already exists, then this operation should return False.

        :param u - A vertex
        :param v - Another vertex
        :return true if the edge was successfully fixed, else false.
        """

        # TODO implement me please.
        pass

    def block_edge(self, u: Vertex, v: Vertex) -> bool:
        """
        Blocks the edge between two vertices, u and v.
        Removes the edge if it exists.
        If not, it should be unsuccessful.

        :param u - A vertex
        :param v - Another vertex.
        :return true if the edge was successfully removed, else false.
        """

        # TODO implement me, please!
        pass

    def find_path(
            self,
            s: Vertex,
            t: Vertex,
            k: int
    ) -> Union[List[Vertex], None]:
        """
        find_path returns a SIMPLE path between `s` and `t` such that from any
        location with food along this path we reach the next location with food
        in at most `k` steps

        :param s - The start vertex for the quokka colony
        :param t - The destination for the quokka colony
        :param k - The maximum number of hops between locations with food, so
        that the colony can survive!
        :returns
            * The list of vertices to form the simple path from `s` to `t`
            satisfying the conditions.
            OR
            * None if no simple path exists that can satisfy the conditions, or
            is invalid.

        Example:
        (* means the vertex has food)
                    *       *
            A---B---C---D---E

            1/ find_path(s=A, t=E, k=2) -> returns: [A, B, C, D, E]

            2/ find_path(s=A, t=E, k=1) -> returns: None
            (because there isn't enough food!)

            3/ find_path(s=A, t=C, k=4) -> returns: [A, B, C]

        """

        # TODO implement me please
        pass

    def exists_path_with_extra_food(
        self,
        s: Vertex,
        t: Vertex,
        k: int,
        x: int
    ) -> bool:
        """
        Determines whether it is possible for the quokkas to make it from s to
        t along a SIMPLE path where from any location with food we reach the
        next location with food in at most k steps, by placing food at at most
        x new locations.

        :param s - The start vertex for the quokka colony
        :param t - The destination for the quokka colony
        :param k - The maximum number of hops between locations with food, so
        that the colony can survive!
        :param x - The number of extra foods to add.
        :returns
            * True if with x added food we can complete the simple path
            * False otherwise.

        Example:
        (* means the vertex has food)
                            *
            A---B---C---D---E

            1/ exists_with_extra_food(A, E, 2, 0) -> returns: False
                (because we can't get from A to E with k=2 and 0 extra food)

            2/ exists_with_extra_food(A, E, 2, 1) -> returns: True
                (Yes, if we put food on `C` then we can get to E with k=2)

            3/ exists_with_extra_food(A, E, 1, 6) -> returns: True
                (Yes, if we put food on `B`, `C`, `D` then we reach E!)
        """

        # TODO implement me please
        pass

    def find_location_of_extra_food(
        self,
        s: Vertex,
        t: Vertex,
        k: int,
        x: int
    ) -> Union[List[Vertex], None]:
        """
        Returns the (at most) x locations where we can add food, such that
        afterwards there exists a path from s to t such that from any location
        with food, we reach the next location with food in at most k steps.

        :param s - The start vertex for the quokka colony
        :param t - The destination for the quokka colony
        :param k - The maximum number of hops between locations with food, so
                    that the colony can survive!
        :param x - The maximum number of extra foods to add.
        :returns:
                * The list of vertices to add the food, in any order :)
                * None if no path exists.

        Example:
        (* means the vertex has food)
                            *
            A---B---C---D---E

            1/ find_location_of_extra_food(A, E, 2, 0) -> returns: None
                (because we can't get from A to E with k=2 and 0 extra food)

            2/ find_location_of_extra_food(A, E, 2, 1) -> returns: [C]
                (If we put food on `C` then we can get to E with k=2)

            3/ find_location_of_extra_food(A, E, 1, 6) -> returns: [B, C, D]
                (Yes, if we put food on `B`, `C`, `D` then we reach E!)

            4/ find_location_of_extra_food(A, E, 2, 10)
                    -> returns: [C] OR [C, D] OR [B, D] OR [B, C] OR [B, C, D]
                (Any of the returned lists satisfy the criteria.)
        """
        # TODO implement me.
        pass

    def minimize_extra_food(
        self,
        s: Vertex,
        t: Vertex,
        k: Vertex
    ) -> Union[List[Vertex], None]:
        """
        Returns the smallest x locations such that adding food at these x
        locations guarantees that there exists a path from s to t such that
        from any location with food, we reach the next location with food in at
        most k steps.

        :param s - The start vertex for the quokka colony.
        :param t - The destination vertex for the quokka colony.
        :param k - The maximum number of hops between
        :returns:
            * The minimum list of locations to place foods in at most K
            steps.
            * None if no path exists.

        Example:
        (* means the vertex has food)
                            *
            A---B---C---D---E

            1/ minimize_extra_food(A, E, 2) -> [C]
            2/ minimize_extra_food(A, E, 1) -> [B, C, D]

        """
        # TODO implement me
        pass
