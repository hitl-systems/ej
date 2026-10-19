"""ej.pack.write.nonfinite_tensors: a weights directory with NaN or inf in a float tensor is reported, one with finite tensors is not."""
import os

import numpy as np
import pytest

pytest.importorskip('safetensors')
from safetensors.numpy import save_file  # noqa: E402

from ej.pack import write  # noqa: E402


def _dir(tmp_path, state_arr):
    os.makedirs(tmp_path / 'encoder')
    save_file({'t0': np.zeros(3, dtype=np.float32), 't1': state_arr}, str(tmp_path / 'state.safetensors'))
    save_file({'e0': np.ones(2, dtype=np.float32)}, str(tmp_path / 'encoder' / 'w23.safetensors'))
    return str(tmp_path)


def test_finite_weights_are_clean(tmp_path):
    assert write.nonfinite_tensors(_dir(tmp_path, np.arange(5, dtype=np.float32))) == {}


def test_nan_and_inf_are_counted_per_tensor(tmp_path):
    a = np.array([0.0, np.nan, np.inf, 1.0, np.nan], dtype=np.float32)
    assert write.nonfinite_tensors(_dir(tmp_path, a)) == {'state/t1': 3}


def test_integer_tensors_are_ignored(tmp_path):
    assert write.nonfinite_tensors(_dir(tmp_path, np.arange(4, dtype=np.int32))) == {}
