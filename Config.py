class FLAGS:
	data_url = ""
	data_dir = None

	background_volume = 0.1
	background_frequency = 0
	silence_percentage = 10.0
	unknown_percentage = 10.0
	time_shift_ms = 0
	use_custom_augs = False

	testing_percentage = 10
	validation_percentage = 10

	sample_rate = 16000
	clip_duration_ms = 1000
	window_size_ms = 30
	window_stride_ms = 10
	dct_coefficient_count = 40

	model_architecture = "ds_cnn"
	model_size_info = [128, 128, 128]
	start_checkpoint = ""

	eval_step_interval = 400
	how_many_training_steps = [5000, 5000]
	learning_rate = [0.001, 0.0001]
	batch_size = 100

	wanted_words = ""
	excluded_words = ""

	summaries_dir = None
	train_dir = None
	save_step_interval = 100

	check_nans = False