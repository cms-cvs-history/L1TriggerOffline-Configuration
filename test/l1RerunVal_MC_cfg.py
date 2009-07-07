import FWCore.ParameterSet.Config as cms

from L1TriggerOffline.Configuration.l1RerunVal_cfg import *

process.TFileService.fileName = 'l1RerunVal_MC.root'

process.GlobalTag.globaltag = "MC_31X_V1::All"

process.load("L1TriggerConfig.GctConfigProducers.l1GctConfig_cfi")


