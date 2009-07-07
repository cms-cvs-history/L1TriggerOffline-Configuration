import FWCore.ParameterSet.Config as cms

from L1TriggerOffline.Configuration.l1RerunVal_cfg import *

process.TFileService.fileName = 'l1RerunVal_STARTUP.root'

process.GlobalTag.globaltag = "STARTUP31X_V1::All"

