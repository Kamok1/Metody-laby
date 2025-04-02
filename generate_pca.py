import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


def plot_pca(df, attributes, n_components=2, exclude_enrolled=True):
    if exclude_enrolled:
        df_filtered = df[df['Target'] != 'Enrolled'].copy()
    else:
        df_filtered = df.copy()

    features_df = df_filtered[attributes].copy()
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features_df)
    pca = PCA(n_components=n_components)

    pca_result = pca.fit_transform(scaled_features)
    pca_df = pd.DataFrame(data=pca_result,columns=[f'PC{i + 1}' for i in range(n_components)])
    pca_df['Target'] = df_filtered['Target'].values

    plt.figure(figsize=(14, 7))
    sns.scatterplot(x='PC1', y='PC2', data=pca_df, hue='Target', alpha=0.5)

    if exclude_enrolled:
        plt.title('PCA of Features (without Enrolled)')
    else:
        plt.title('PCA of Features')

    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.legend(title='Target')

    os.makedirs('plots/pca', exist_ok=True)
    suffix = "_exclude_enrolled" if exclude_enrolled else ""
    plt.savefig(f'plots/pca/pca{n_components}_plot{suffix}.png', dpi=300)
    plt.close()
