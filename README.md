# A-K-means-clustering-algorithm-to-group-customers-of-a-retail-store-based-on-their-purchase-history

Mall Customer Segmentation

This project is a Python-based customer segmentation model using K-means clustering. It leverages scikit-learn, pandas, and matplotlib to segment mall customers based on their annual income and spending score from a dataset (Mall_Customers.csv). The model identifies customer groups, visualizes clusters, and saves results.

Features





Data Preprocessing: Standardizes features (Annual Income, Spending Score) for effective clustering.



Elbow Method: Determines the optimal number of clusters by plotting Within-Cluster Sum of Squares (WCSS).



K-means Clustering: Segments customers into 5 clusters based on income and spending behavior.



Visualization: Generates plots for the elbow curve (elbow_curve.png) and cluster distribution (customer_clusters.png).



Output: Saves the dataset with cluster labels (Mall_Customers_Clustered.csv) and prints cluster characteristics.

Prerequisites





Python 3.8 or higher



A dataset (Mall_Customers.csv) with columns: Annual Income (k$) and Spending Score (1-100). Example: Kaggle Mall Customer Segmentation Dataset

Installation





Clone the repository:

git clone <repository-url>
cd mall-customer-segmentation



Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate



Install the required dependencies:

pip install -r requirements.txt



Place the Mall_Customers.csv dataset in the specified directory (e.g., D:\mall customer segmentation\Mall_Customers.csv) or update the file path in the script.

Usage





Ensure the Mall_Customers.csv dataset is accessible.



Run the script:

python customer_segmentation.py



The script will:





Load and preprocess the dataset.



Apply K-means clustering with 5 clusters.



Save the elbow curve (elbow_curve.png) and cluster visualization (customer_clusters.png).



Save the clustered dataset (Mall_Customers_Clustered.csv).



Print characteristics for each cluster (size, average income, spending score).



View the generated plots and output file in the project directory.

Example Output

Cluster Characteristics:

Cluster 0:
Number of customers: 40
Average Annual Income: $87.75k
Average Spending Score: 17.55

Cluster 1:
Number of customers: 35
Average Annual Income: $24.66k
Average Spending Score: 20.91
...





Plots: elbow_curve.png shows the WCSS for 1-10 clusters; customer_clusters.png visualizes customer segments with centroids.



Output File: Mall_Customers_Clustered.csv contains the original data with an additional Cluster column.

Project Structure





customer_segmentation.py: Main script containing the clustering logic.



requirements.txt: List of Python dependencies.



Mall_Customers.csv: Dataset file (not included; must be provided by the user).



elbow_curve.png: Generated elbow method plot.



customer_clusters.png: Generated cluster visualization.



Mall_Customers_Clustered.csv: Output dataset with cluster labels.

Dependencies

See requirements.txt for the full list of dependencies, including:





pandas: For data loading and manipulation.



numpy: For numerical computations.



scikit-learn: For K-means clustering and data scaling.



matplotlib: For plotting the elbow curve and clusters.

Notes





Ensure the Mall_Customers.csv file path in the script matches your local setup.



The number of clusters (5) is chosen based on the elbow method; adjust if needed by inspecting elbow_curve.png.



The script assumes no missing values in the dataset; add preprocessing steps if necessary.



Cluster characteristics help identify customer segments (e.g., high-income, high-spending vs. low-income, low-spending).

Troubleshooting





File Not Found Error: Verify the Mall_Customers.csv path is correct and the file exists.



Dependency Issues: Ensure all packages in requirements.txt are installed (pip install -r requirements.txt).



Plot Issues: Check that matplotlib is correctly installed and the output directory is writable.
