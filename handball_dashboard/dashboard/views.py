from django.shortcuts import render
from .models import Player, PlayerStats, Game
from django.http import JsonResponse
import joblib

# Dashboard view that lists all players and their stats
def dashboard_view(request):
    players = Player.objects.all()
    stats = PlayerStats.objects.all()
    return render(request, 'dashboard.html', {'players': players, 'stats': stats})

# Player detail view
def player_detail_view(request, player_id):
    player = Player.objects.get(id=player_id)
    stats = PlayerStats.objects.filter(player=player)
    return render(request, 'player_detail.html', {'player': player, 'stats': stats})

# AI Prediction view (example)
def predict_performance(request, player_id):
    player_stats = PlayerStats.objects.filter(player_id=player_id)
    
    # Load pre-trained model
    model = joblib.load('model.joblib')  # Replace with actual file path and model name
    
    # Preprocess player stats data
    # (e.g., normalize, handle missing values, etc.)
    # This step depends on the actual model used for prediction
    

    # Assume we use player stats to predict performance
    prediction = model.predict([[stat.goals for stat in player_stats]])  # Adjust based on actual model input format
    
    return JsonResponse({'prediction': prediction.tolist()})



from django.shortcuts import render
import joblib

def predict_performance(request):
    # Cargar el modelo
    model = joblib.load('models/model.pkl')

    # Realizar una predicción con datos de prueba (esto debería venir de la base de datos o de un formulario)
    predictions = model.predict([[4, 3, 1, 2]])  # Ejemplo de datos de un jugador

    return render(request, 'result.html', {'predictions': predictions})
from django.shortcuts import render
import joblib

# Cargar el modelo previamente entrenado
model = joblib.load('models/model.pkl')

def dashboard(request):
    predictions = None
    if request.method == 'POST':
        # Recoger los datos del formulario
        goals = int(request.POST.get('goals'))
        assists = int(request.POST.get('assists'))
        blocks = int(request.POST.get('blocks'))
        saves = int(request.POST.get('saves'))

        # Realizar la predicción
        prediction = model.predict([[goals, assists, blocks, saves]])

        # Pasar la predicción a la plantilla
        predictions = prediction[0]

    return render(request, 'dashboard.html', {'predictions': predictions})
