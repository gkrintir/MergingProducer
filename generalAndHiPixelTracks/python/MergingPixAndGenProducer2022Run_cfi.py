import FWCore.ParameterSet.Config as cms

generalAndHiPixelTracks = cms.EDProducer('generalAndHiPixelTracks',
  genTrackSrc = cms.InputTag("generalTracks"),
  pixTrackSrc = cms.InputTag("hiConformalPixelTracks"),
  vertexSrc = cms.InputTag("offlinePrimaryVertices"),
  centralitySrc = cms.InputTag("centralityBin","HFtowers"),
  caloTower = cms.InputTag('towerMaker'),
  mvaSrc = cms.InputTag('generalTracks','MVAValues'),
  cutWidth = cms.double(0.2),
  trkRes = cms.double(0.02),
  qualityString = cms.string("highPurity"),
  dxyErrMax = cms.double(3.0),
  dzErrMax = cms.double(3.0),
  ptErrMax = cms.double(0.1),
  nhitsMin = cms.int32(0),
  chi2nMax = cms.double(0.18),
  chi2nMaxPixel = cms.double(9999.0),
  dzErrMaxPixel = cms.double(3.0),
  dxyErrMaxPixel = cms.double(3.0)
) 
