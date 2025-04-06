import pandas as pd
from mplsoccer import Pitch
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rc
import os

def animLoad(startF, endF, outFile):
  frames = pd.read_csv("./sporting_college_data_1846146_tracking.csv")
  pitch = Pitch(pitch_type='skillcorner', pitch_length=105, pitch_width=68, pitch_color="green", stripe=False, line_color='white')
  fig, ax = pitch.draw(figsize=(16, 10.4))

  marker_kwargs = {'marker': 'o', 'markeredgecolor': 'black', 'linestyle': 'None'}
  ball, = ax.plot([], [], ms=12, markerfacecolor='w', zorder=3, **marker_kwargs)
  home, = ax.plot([], [], ms=16, markerfacecolor='red', **marker_kwargs)
  away, = ax.plot([], [], ms=16, markerfacecolor='skyblue', **marker_kwargs)

  def plot_frame(f):
    current_frame = frames[(frames.frame_id == f)]
    player_pos = current_frame[(current_frame.player_id != "ball")]
    ball_pos = current_frame[current_frame.player_id == "ball"]
    ball.set_data(ball_pos['x'], ball_pos['y'])
    away.set_data(
        player_pos.loc[player_pos.team_id == 2337.0, 'x'],
        player_pos.loc[player_pos.team_id == 2337.0, 'y']
    )
    home.set_data(
        player_pos.loc[player_pos.team_id == 2334.0, 'x'],
        player_pos.loc[player_pos.team_id == 2334.0, 'y']
    )
    return ball, away, home

  # Animation setup
  rc('animation', html='jshtml')

  # Create an animation object
  anim = animation.FuncAnimation(
    fig, 
    plot_frame, 
    frames=list(range(startF, endF)), 
    interval=100, 
    blit=True
  )

  # Save the animation as an HTML file
  if not os.path.exists('static/'):
    os.makedirs('static')
  
  anim.save(f'static/{outFile}', writer='html', fps=20)
  print("done running")
  return "Ran!"

#animLoad(5698, 5810, "test1.html") nuts highlight









#animLoad(22930, 23050, "pressure6.html")
# animLoad(22955, 23026, "pressure28.html")
# animLoad(24022, 24058, "pressure29.html")
# animLoad(28146, 28205, "pressure30.html")
# animLoad(35463, 35521, "pressure31.html")
# animLoad(43650, 43727, "pressure32.html")
# animLoad(44223, 44410, "pressure33.html")
# animLoad(46336, 46400, "pressure34.html")
# animLoad(50641, 50673, "pressure35.html")
# animLoad(54202, 54326, "pressure36.html")

#animLoad(52900, 53035, "threat2.html")
#animLoad(5673, 5835, "threat1.html")
# animLoad(7786, 7952, "threat3.html")
# animLoad(13307, 13484, "threat4.html")
# animLoad(13718, 13862, "threat5.html")
# animLoad(15240, 15360, "threat6.html")
# # animLoad(17951, 18138, "pressure1.html")
# # animLoad(22930, 23051, "pressure2.html") #best pass
# # animLoad(23997, 24083, "pressure3.html")
# animLoad(26136, 26244, "threat7.html")
# # animLoad(28121, 28230, "pressure4.html")
# animLoad(33501, 33616, "threat8.html")
# animLoad(33979, 34091, "threat9.html")
# # animLoad(35438, 35546, "pressure5.html")
# animLoad(35434, 35571, "threat10.html")
# animLoad(36321, 36477, "threat11.html")
# # animLoad(43625, 43752, "pressure6.html")
# # animLoad(44198, 44435, "pressure7.html") #best pass
# animLoad(44689, 44801, "threat12.html")
# # animLoad(46311, 46425, "pressure8.html")
# # animLoad(50616, 50698, "pressure9.html")
# animLoad(50857, 51036, "threat13.html")
# animLoad(51108, 51260, "threat14.html")
# animLoad(52900, 53035, "threat15.html")
# # animLoad(54177, 54351, "pressure10.html")
# animLoad(57823, 57979, "threat16.html")
# animLoad(58777, 58920, "threat17.html")
