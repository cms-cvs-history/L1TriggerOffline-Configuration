import FWCore.ParameterSet.Config as cms

from L1TriggerOffline.Configuration.l1RerunVal_cfg import *

process.GlobalTag.globaltag = "IDEAL_31X::All"

from CondTools.L1Trigger.L1CondDBSource_cff import initCondDBSource
initCondDBSource( process,
                  inputDBConnect = 'sqlite_file:/afs/cern.ch/user/w/wsun/public/conddb/l1config31XV10.db',
                  tagBase = 'IDEAL',
                  includeAllTags = True )

