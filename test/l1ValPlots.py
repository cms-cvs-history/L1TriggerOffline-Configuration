# l1ValPlots.py
# Jim Brooke
#
# Usage :
#   eval `scramv1 ru -sh`
#   python l1ValPlots.py <input histogram file> <output plot filename>
#


import sys;
import os;
import tarfile;

hfilename = sys.argv[1];
pfilename = sys.argv[2];

from ROOT import *;
gSystem.Load("libFWCoreFWLite.so");
AutoLibraryLoader.enable();

gROOT.Reset();

def plot(file, hist, xLabel, yLabel="Events", Opt=""):
	H = file.Get(hist);
	H.GetXaxis().SetTitle(xLabel);
	H.GetYaxis().SetTitle(yLabel);
	H.Draw(Opt);

# Basic plots
def basicPlots(obj, dir):
	pdf = TPDF(obj+".pdf");

	plot(hfile,dir+"/L1Candidates/Et","E_{T}","No. of entries");
	canvas.Update();
#	canvas.Print(obj+".ps(");

       	plot(hfile,dir+"/L1Candidates/Eta","#eta","No. of entries");
	canvas.Update();
#	canvas.Print(obj+".ps(");

	plot(hfile,dir+"/L1Candidates/Phi","#phi","No. of entries");
	canvas.Update();
#	canvas.Print(obj+".ps(");

	plot(hfile,dir+"/Resolutions/EtRes","(E_{T,L1}-E_{T,Ref})/E_{T,Ref}","No. of entries");
	canvas.Update();
#	canvas.Print(obj+".ps(");

	plot(hfile,dir+"/Resolutions/EtCor","E_{T, Ref} (GeV)","E_{T, L1} (GeV)");
	canvas.Update();
#	canvas.Print(obj+".ps(");

	plot(hfile,dir+"/Resolutions/EtaRes","(#eta_{L1}-#eta_{Ref})/#eta_{Ref}","No. of entries");
	canvas.Update();
#	canvas.Print(obj+".ps(");

	plot(hfile,dir+"/Resolutions/EtaCor","#eta_{Ref}","#eta_{L1}");
	canvas.Update();
#	canvas.Print(obj+".ps(");

	plot(hfile,dir+"/Resolutions/PhiRes","(#phi_{L1}-#phi_{Ref})/#phi_{Ref}","No. of entries");
	canvas.Update();
#	canvas.Print(obj+".ps(");

	plot(hfile,dir+"/Resolutions/PhiCor","#phi_{Ref} (rad)","#phi_{L1} (rad)");
	canvas.Update();
#	canvas.Print(obj+".ps(");

	plot(hfile,dir+"/Efficiencies/EtEff","E_{T} (GeV)","Efficiency","e");
	canvas.Update();
#	canvas.Print(obj+".ps(");

	plot(hfile,dir+"/Efficiencies/EtaEff","#eta","Efficiency","e");
	canvas.Update();
#	canvas.Print(obj+".ps(");

	plot(hfile,dir+"/Efficiencies/PhiEff","#phi (rad)","Efficiency","e");
	canvas.Update();
#	canvas.Print(obj+".ps)");
	pdf.Close();

# open file
hfile = TFile(hfilename);
print "Making plots for "+hfilename;

# canvas
canvas = TCanvas("canvas");

basicPlots("muon", "L1AnalyzerMuonMC");
basicPlots("em", "L1AnalyzerEmMC");
basicPlots("isoem", "L1AnalyzerIsoEmMC");
basicPlots("nonisoem", "L1AnalyzerNonIsoEmMC");
basicPlots("jet", "L1AnalyzerJetsMC");
basicPlots("cenjet", "L1AnalyzerCenJetsMC");
basicPlots("forjet", "L1AnalyzerForJetsMC");
basicPlots("tau", "L1AnalyzerTauJetsMC");
basicPlots("met", "L1AnalyzerMetMC");

# make tarfile
objs = ["muon", "em", "isoem", "nonisoem", "jet", "cenjet", "forjet", "tau", "met"];

t = tarfile.open(name = pfilename+".tgz", mode = 'w:gz')
for obj in objs:
	t.add(obj+".pdf");
t.close()

# cleanup
for obj in objs:
	os.remove(obj+".pdf");
