setup(
    entry_points={
        'nbconvert.exporters': [
            'r = nbconvert_exporter_r:RExporter'
        ],
    }
)
