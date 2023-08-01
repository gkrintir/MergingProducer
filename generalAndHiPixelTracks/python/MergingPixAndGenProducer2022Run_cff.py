import FWCore.ParameterSet.Config as cms

from MergingProducer.generalAndHiPixelTracks.MergingPixAndGenProducer2022Run_cfi import *

generalAndHiPixelTracksLoose = generalAndHiPixelTracks.clone()
generalAndHiPixelTracksLoose.dxyErrMax = cms.double(5.0)
generalAndHiPixelTracksLoose.dzErrMax = cms.double(5.0)
generalAndHiPixelTracksLoose.ptErrMax = cms.double(0.15)
generalAndHiPixelTracksLoose.nhitsMin = cms.int32(11)
generalAndHiPixelTracksLoose.chi2nMax = cms.double(0.18)
generalAndHiPixelTracksLoose.dzErrMaxPixel = cms.double(3.0)
generalAndHiPixelTracksLoose.dxyErrMaxPixel = cms.double(3.0)


generalAndHiPixelTracksTight = generalAndHiPixelTracks.clone()
generalAndHiPixelTracksTight.dxyErrMax = cms.double(2.0)
generalAndHiPixelTracksTight.dzErrMax = cms.double(2.0)
generalAndHiPixelTracksTight.ptErrMax = cms.double(0.05)
generalAndHiPixelTracksTight.nhitsMin = cms.int32(11)
generalAndHiPixelTracksTight.chi2nMax = cms.double(0.15)
generalAndHiPixelTracksTight.dzErrMaxPixel = cms.double(1.0)
generalAndHiPixelTracksTight.dxyErrMaxPixel = cms.double(1.0)

