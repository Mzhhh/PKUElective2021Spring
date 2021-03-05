import os
from ..utils import xMD5

class Captcha(object):

    __slots__ = ['_code','_original','_denoised','_segments','_spans']

    def __init__(self, code, original, denoised, segments, spans):
        self._code = code
        self._original = original
        self._denoised = denoised
        self._segments = segments
        self._spans = spans

    @property
    def code(self):
        return self._code

    @property
    def original(self):
        return self._original

    @property
    def denoised(self):
        return self._denoised

    @property
    def segments(self):
        return self._segments

    @property
    def spans(self):
        return self._spans

    def __repr__(self):
        return '%s(%r)' % (
            self.__class__.__name__,
            self._code,
        )

    def save(self, folder):
        code = self._code
        oim = self._original
        dim = self._denoised
        segs = self._segments
        spans = self._spans
        md5 = xMD5(oim.tobytes())

        oim.save(os.path.join(folder, "%s_original_%s.jpg" % (code, md5)))
        dim.save(os.path.join(folder, "%s_denoised_%s.jpg" % (code, md5)))
        for im, (st, ed), c in zip(segs, spans, code):
            im.save(os.path.join(folder, "%s_%s_(%d,%d)_%s.jpg" % (code, c, st, ed, md5)))