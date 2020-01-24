import FWCore.ParameterSet.Config as cms


from RecoLocalCalo.HGCalRecProducers.HGCalRecHit_cfi import dEdX_weights_v10, HGCalRecHit
from RecoLocalCalo.HGCalRecProducers.HGCalUncalibRecHit_cfi import fCPerMIP_v9 ##same as v10 - 13/01/2020
from SimCalorimetry.HGCalSimProducers.hgcalDigitizer_cfi import HGCAL_noise_fC, HGCAL_noise_heback, hgceeDigitizer, hgchefrontDigitizer, hgchebackDigitizer, nonAgedNoises, endOfLifeNoises

HGCalTimeEstimator = cms.PSet(
    dEdXweights = cms.vdouble(dEdX_weights_v10),
    thicknessCorrection = cms.vdouble(0.781,0.775,0.769), #from  HGCalRecHit.thicknessCorrection v10
    HGCEE_fCPerMIP = cms.vdouble(fCPerMIP_v9),
    
    timeOFFSET = hgceeDigitizer.tofDelay,

    HGCEE_noisefC = cms.vdouble(HGCAL_noise_fC.values),
    HGCEF_noisefC = cms.vdouble(HGCAL_noise_fC.values), ##same as EE
    HGCBH_noiseMIP = cms.double(0.01), ##BH
    
    nonAgedNoises = cms.vdouble(nonAgedNoises),
    endOfLifeNoises = cms.vdouble(endOfLifeNoises),

    HGCEE_keV2fC  = hgceeDigitizer.digiCfg.keV2fC,
    HGCHEF_keV2fC = hgchefrontDigitizer.digiCfg.keV2fC,
    HGCHB_keV2MIP = hgchebackDigitizer.digiCfg.keV2MIP ##BH
    )


