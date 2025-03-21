from flask import Blueprint, request, jsonify
import networkx as nx

# Create a Flask Blueprint
recommend_bp = Blueprint('recommend', __name__)

# Sample Graph of Users and Connections
social_graph = nx.Graph()
sample_edges = [
    (1, 2), (1, 3), (2, 4), (2, 5), (3, 5), 
    (4, 6), (5, 6), (5, 7), (6, 8), (7, 8)
]
social_graph.add_edges_from(sample_edges)

# Function to calculate Jaccard Coefficient
def jaccard_recommendations(user):
    preds = nx.jaccard_coefficient(social_graph, [(user, n) for n in social_graph.nodes if n != user])
    return sorted(preds, key=lambda x: x[2], reverse=True)[:5]  # Top 5

# Function to calculate Adamic/Adar Index
def adamic_adar_recommendations(user):
    preds = nx.adamic_adar_index(social_graph, [(user, n) for n in social_graph.nodes if n != user])
    return sorted(preds, key=lambda x: x[2], reverse=True)[:5]

# Function to calculate Personalized PageRank
def personalized_pagerank_recommendations(user):
    pagerank_scores = nx.pagerank(social_graph, alpha=0.85, personalization={user: 1})
    sorted_users = sorted(pagerank_scores.items(), key=lambda x: x[1], reverse=True)
    return [u for u, _ in sorted_users if u != user][:5]  # Exclude the user

# API Endpoint to Get Friend Recommendations
@recommend_bp.route('/recommend', methods=['GET'])
def recommend():
    user = int(request.args.get('user'))
    
    if user not in social_graph.nodes:
        return jsonify({"error": "User not found"}), 404

    jaccard = jaccard_recommendations(user)
    adamic_adar = adamic_adar_recommendations(user)
    pagerank = personalized_pagerank_recommendations(user)

    recommendations = {
        "jaccard_coefficient": [(a, b, round(score, 3)) for a, b, score in jaccard],
        "adamic_adar_index": [(a, b, round(score, 3)) for a, b, score in adamic_adar],
        "personalized_pagerank": pagerank
    }

    return jsonify(recommendations)
