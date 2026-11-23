def k_means_clustering(
    points: list[tuple[float, ...]],
    k: int,
    initial_centroids: list[tuple[float, ...]],
    max_iterations: int
) -> list[tuple[float, ...]]:

    centroids = [tuple(c) for c in initial_centroids]

    for _ in range(max_iterations):
        clusters = [[] for _ in range(k)]

        # Step 1: Assign each point to its nearest centroid
        for point in points:
            distances = [
                sum((point[d] - centroid[d]) ** 2
                    for d in range(len(point)))
                for centroid in centroids
            ]

            closest_cluster = distances.index(min(distances))
            clusters[closest_cluster].append(point)

        # Step 2: Recalculate centroids
        new_centroids = []

        for i in range(k):
            if clusters[i]:
                dimensions = len(centroids[i])

                new_centroid = tuple(
                    sum(point[d] for point in clusters[i]) / len(clusters[i])
                    for d in range(dimensions)
                )
                new_centroids.append(new_centroid)
            else:
                # Keep the previous centroid if its cluster is empty
                new_centroids.append(centroids[i])

        # Step 3: Stop if centroids no longer change
        if new_centroids == centroids:
            break

        centroids = new_centroids

    # Round each coordinate to 4 decimal places
    final_centroids = [
        tuple(round(value, 4) for value in centroid)
        for centroid in centroids
    ]

    return final_centroids