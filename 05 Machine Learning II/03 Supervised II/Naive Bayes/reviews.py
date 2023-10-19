import pickle

video_game_counter = pickle.load( open( "game_counter.p", "rb" ) )
video_game_training = pickle.load( open( "game_train.p", "rb" ) )
instant_video_counter = pickle.load( open( "video_counter.p", "rb" ) )
instant_video_training = pickle.load( open( "video_train.p", "rb" ) )
baby_counter = pickle.load( open( "baby_counter.p", "rb" ) )
baby_training = pickle.load( open( "baby_train.p", "rb" ) )
