"""The main program that runs closeGraph."""
# -*- coding=utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys

from config import parser
from gspan import gSpan
from closegraph import closeGraph


def main(FLAGS=None):
    """Run closeGraph."""

    if FLAGS is None:
        FLAGS, _ = parser.parse_known_args(args=sys.argv[1:])

    if not os.path.exists(FLAGS.database_file_name):
        print('{} does not exist.'.format(FLAGS.database_file_name))
        sys.exit()

    # gs = gSpan(
    #     database_file_name=FLAGS.database_file_name,
    #     min_support=FLAGS.min_support,
    #     min_num_vertices=FLAGS.lower_bound_of_num_vertices,
    #     max_num_vertices=FLAGS.upper_bound_of_num_vertices,
    #     max_ngraphs=FLAGS.num_graphs,
    #     is_undirected=(not FLAGS.directed),
    #     verbose=FLAGS.verbose,
    #     visualize=FLAGS.plot,
    #     where=FLAGS.where
    # )
    #
    # gs.run()
    # gs.time_stats()
    # return gs

    cg = closeGraph(
        database_file_name=FLAGS.database_file_name,
        min_support=FLAGS.min_support,
        min_num_vertices=FLAGS.lower_bound_of_num_vertices,
        max_num_vertices=FLAGS.upper_bound_of_num_vertices,
        max_ngraphs=FLAGS.num_graphs,
        is_undirected=(not FLAGS.directed),
        verbose=FLAGS.verbose,
        visualize=FLAGS.plot,
        where=FLAGS.where
    )

    cg.run()
    cg.time_stats()

    '''
    db = cg._write_graphs()

    head, tail = os.path.split(FLAGS.database_file_name)

    db_file = open(head + "/normalized_" + tail, "w")
    db_file.write(db)
    db_file.close()
    '''

    closed_graphs = list()
    for g in cg._frequent_subgraphs:
        closed_graphs.append(g)
    closed_graphs.sort(key=lambda x: (x.support_projections, x.get_num_vertices()))
    for g in closed_graphs:
        g.display()
        print("projections ", g.support_projections, " vertices ", g.get_num_vertices())
        print("------------------")
    return cg


if __name__ == '__main__':
    main()
