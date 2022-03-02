from util import openslice, multislice

config = {
    "name": "Oneshot",
    "experiment_name": "EfficientLearning",
    "dataset_path": "./data.pickle",
    "load_pretransformed": True,
    "run_directory": "./runs/efficient/oneshot",
    "plot_directory": "images",
    "load_model": False,
    "continue": False,
    "model_path": "./runs/efficient/base/",
    "mode": "one_shot_inf",
    "test": True,
    "dtw": False,
    "dtw_total": False,
    "epochs": 100,
    "epochs_one_shot_inf": 2000,
    "batch_size": 1,
    "shuffle_test": True,
    "oneshot_batch_size": 1,
    "log_interval": 4,
    "log_readable": False,
    "save_interval": 1,
    "plot_every": 2500,
    "test_plot_every": 250000,
    "threshold": 0.90,
    "filetype": "png",
    "input_size": 62,
    "participant_size": 77,
    "include_participant": True,
    "hidden_size": 100,
    "num_layers": 1,
    "hidden_bias": False,
    "dropout": 0,
    "output_size": 4,
    "output_bias": False,
    "criterion": "mse_loss",
    "optimizer": "adam",
    "lr": 0.001,
    "beta1": 0.9,
    "beta2": 0.999,
    "weight_decay": 0,
    "seed": 12345678,
    "use_cuda": True,
    "participant_bounds": multislice([(0, 75, 1)]),
    "character_bounds": multislice([(10, 23, 1)]),
    "instance_bounds": openslice(),
    "test_participant_bounds": multislice([(1, 2, 1)]),
    "test_character_bounds": multislice([(23, 36, 1)]),
    "test_instance_bounds": multislice([(1, None, 1)]),
    "oneshot_participant_bounds": multislice([(2, 3, 1)]),
    "oneshot_character_bounds": multislice([(23, 36, 1)]),
    "oneshot_instance_bounds": multislice([(2, 3, 1)]),
    "instances": None
}
