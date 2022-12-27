# Welcome to Pycallingcards documentation

Cells do not live in a vacuum, but in a milieu defined by cell–cell
communication that can be quantified via recent advances in spatial
transcriptomics.

Here we present *Pycallingcards*, a open source framework that
welcomes community contributions for quantitative spatiotemporal
modeling of spatial transcriptomics. Leveraging the ultra-high
spatial-resolution, large field of view and high RNA capture sensitivity
of Stereo-seq, *Pycallingcards* enables single cell resolution spatial
transcriptomics via nuclei-staining and RNA signal based cell
segmentation. *Pycallingcards* also delivers novel methods for spatially
constrained clustering to identify continuous tissue domains, spatial
aware differential analyses to reveal spatial gene expression hotspots
and modules, as well as the intricate ligand-receptor interactions.

Importantly, *Pycallingcards* is equipped with sophisticated methods for building
whole-body 3D models of embryogenesis by leveraging serial profilings of
drosophila embryos across different stages. *Pycallingcards* thus enables us to
evolve from the reductionism of single cells to the holisticism of
tissues and organs, heralding a paradigm shift in moving toward studying
the ecology of tissue and organ while still offering us the opportunity
to reveal associated molecular mechanisms.

```{attention}
**Pycallingcards** is currently in beta. Developers are hard at work implementing new features,
fixing bugs, and improving the overall user experience. If you have a feature request
and/or would like to report a bug, please feel free to open an issue on Github.

**Pycallingcards** will not be uploaded to Pypi until its first stable release. In the meantime,
**Pycallingcards** may be installed directly from GitHub using [these instructions](installation.md#github).
```

```{eval-rst}
.. card:: Installation :octicon:`plug;1em;`
    :link: installation
    :link-type: doc

    Click here to view a brief *Pycallingcards* installation guide.
```

```{eval-rst}
.. card:: Tutorials :octicon:`play;1em;`
    :link: tutorials/index
    :link-type: doc

    End-to-end tutorials showcasing key features in the package.
```


```{eval-rst}
.. card:: API reference :octicon:`book;1em;`
    :link: autoapi/Pycallingcards/index
    :link-type: doc

    Detailed descriptions of *Pycallingcards* API and internals.
```

```{eval-rst}
.. card:: GitHub :octicon:`mark-github;1em;`
    :link: https://github.com/The-Mitra-Lab/pycallingcards

    Ask questions, report bugs, and contribute to *Pycallingcards* at our GitHub repository.
```

*This documentation was heavily inspired and adapted from the [spateo documentation](https://spateo-release.readthedocs.io/en/latest/index.html#). Go check them out!*

```{toctree}
:hidden: true
:maxdepth: 3
:titlesonly: true

Documentation home <self>
installation
tutorials/index
API <autoapi/Pycallingcards/index>
references
contributing
GitHub <https://github.com/The-Mitra-Lab/pycallingcards>
```
