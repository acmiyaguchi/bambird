# -*- coding: utf-8 -*-
""" 

"""
from .version import __version__

# -*- coding: utf-8 -*-
""" 
Labelling function
==================

The package ``bambird`` is an ensemble of functions to build a labelling function to clean audio recordings from Xeno-Canto.

Config yaml
-----------
.. autosummary::
    :toctree: generated/
    load_config

Dataset
-------
.. autosummary::
    :toctree: generated/
    query_xc
    download_xc
    query_download_xc
    grab_audio_to_df
    change_path
    
ROIs segmentation
-----------------
.. autosummary::
    :toctree: generated/
    extract_rois_core
    extract_rois_full_sig    
    single_file_extract_rois
    multicpu_extract_rois

ROIs features
-------------
.. autosummary::
    :toctree: generated/
    compute_features
    multicpu_compute_features
    
ROIs clustering
---------------
.. autosummary::
    :toctree: generated/
    find_cluster
    cluster_eval
    overlay_rois
    mark_rois
    unmark_rois

"""

from .segmentation_extract_rois_full_sig import(       
    extract_rois_full_sig,
    )

from .segmentation_extract_rois_core import(       
    extract_rois_core,
    )

from .config import (
    load_config
    )

from .dataset import(
    grab_audio_to_df,
    change_path,
    query_xc,
    download_xc,
    query_download_xc,
    )

from .segmentation import(     
    single_file_extract_rois,
    multicpu_extract_rois,
    )


from .features import(
    compute_features,
    multicpu_compute_features,
    )
                 
def __getattr__(name):
    """Lazy import for cluster module (umap/hdbscan are slow to import)."""
    _cluster_names = {'find_cluster', 'cluster_eval', 'overlay_rois', 'mark_rois', 'unmark_rois'}
    if name in _cluster_names:
        from . import cluster as _cluster
        return getattr(_cluster, name)
    raise AttributeError(f"module 'bambird' has no attribute {name!r}")


__all__ = [
        # config.py
        'load_config',
        # dataset.py
        'grab_audio_to_df',
        'change_path',
        'query_xc',
        'download_xc',
        'query_download_xc',
        # segmentation.py                         
        'extract_rois_core',
        'extract_rois_full_sig',
        'single_file_extract_rois',
        'multicpu_extract_rois',
        # features.py
        'compute_features',
        'multicpu_compute_features',
        # cluster.py
        'find_cluster',
        'cluster_eval',
        'overlay_rois',
        'mark_rois',
        'unmark_rois'
        ]


