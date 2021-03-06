# Copyright (c) 2018, NVIDIA CORPORATION. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#  * Neither the name of NVIDIA CORPORATION nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import numpy as np

_last_request_id = 0

def validate_for_tf_model(input_dtype, output0_dtype, output1_dtype):
    """Return True if input and output dtypes are supported by a TF model."""
    return True

def validate_for_c2_model(input_dtype, output0_dtype, output1_dtype):
    """Return True if input and output dtypes are supported by a Caffe2 model."""

    # Some operations used by test don't support fp16.
    if ((input_dtype == np.float16) or (output0_dtype == np.float16) or
        (output1_dtype == np.float16)):
        return False

    # Some operations don't support any int type except int32.
    if ((input_dtype == np.int8) or (output0_dtype == np.int8) or
        (output1_dtype == np.int8) or (input_dtype == np.int16) or
        (output0_dtype == np.int16) or (output1_dtype == np.int16)):
        return False

    return True

def validate_for_trt_model(input_dtype, output0_dtype, output1_dtype):
    """Return True if input and output dtypes are supported by a TRT model."""

    # TRT supports limited datatypes as of TRT 4.0. Input can be FP16 or
    # FP32, output must be FP32.
    if (input_dtype != np.float16) and (input_dtype != np.float32):
        return False
    if (output0_dtype != np.float32) or (output1_dtype != np.float32):
        return False
    return True

def validate_for_custom_model(input_dtype, output0_dtype, output1_dtype):
    """Return True if input and output dtypes are supported by custom model."""

    # The custom model is src/custom/addsub... it only supports int32
    if input_dtype != np.int32:
        return False
    if (output0_dtype != np.int32) or (output1_dtype != np.int32):
        return False
    return True

def get_model_name(pf, input_dtype, output0_dtype, output1_dtype):
    return "{}_{}_{}_{}".format(
        pf, np.dtype(input_dtype).name, np.dtype(output0_dtype).name,
        np.dtype(output1_dtype).name)
