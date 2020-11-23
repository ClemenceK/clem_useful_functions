#############################################################################
#########useful dataviz functions coded during Wagon bootcamp################
#############################################################################


def features_boxplots(df, n_rows=4, n_cols=4, figsize=(20,10)):
    """displays a boxplot for each feature not of type "object"
        can be useful to discover outliers and decide how to scale a feature
        df: a dataframe with the features to graph
        n_rows and n_cols: number of rows and columns to use for the plotting
        figsize

        returns None"""
    import seaborn as sns
    import matplotlib.pyplot as plt
    import math

    list_features = df.columns[df.dtypes != object]

    if  len(list_features) > n_rows*n_cols:
        raise Exception(f'Asking to show {len(list_features)} features \
            on {n_rows} rows * {n_cols} cols. Adjust n_rows and n_cols arguments.')

    fig = plt.figure(figsize=figsize, tight_layout=True)

    for i, feature in enumerate(list_features):
        sns.boxplot(x=df[feature], ax=fig.add_subplot(n_rows,n_cols,i+1))
        plt.gca().set_title(feature, size=14)

    return None


def features_histplots(df, n_rows=4, n_cols=4, figsize=(20,10), numerical_only=False):
    """displays a histplot for each feature of the dataset
        df: a dataframe
        n_rows and n_cols: number of rows and columns to use for the plotting
        figsize
        numerical_only: if True, doesn't plot "object" types features

        returns None"""
    import seaborn as sns
    import matplotlib.pyplot as plt
    import math


    if numerical_only:
        list_features = list_features = df.columns[df.dtypes != object]
    else:
        list_features = df.columns

    if  len(list_features) > n_rows*n_cols:
        raise Exception(f'Asking to show {len(list_features)} features\
            on {n_rows} rows * {n_cols} cols. Adjust n_rows and n_cols arguments.')

    fig = plt.figure(figsize=figsize, tight_layout=True)

    for i, feature in enumerate(list_features):
        sns.histplot(x=df[feature], ax=fig.add_subplot(n_rows,n_cols,i+1))
        plt.gca().set_title(feature, size=16)

    return None


