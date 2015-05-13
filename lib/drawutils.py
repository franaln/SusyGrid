import ROOT
from rootutils import *

def draw_boxlegend(x, y, color, text):

    box = ROOT.TBox(x, y+2, x+30, y+28)
    box.SetFillColor(get_color(color))

    label = ROOT.TLatex(x+40, y, text)
    label.SetTextSize(0.025)

    ROOT.SetOwnership(box, False)
    ROOT.SetOwnership(label, False)

    box.Draw()
    label.Draw()

def draw_boxpie(m3, mu, *brs):

    y1 = mu
    y2 = mu + 25

    colors = ['purple', 'blue', 'green', 'orange', 'pink']

    x2 = m3
    for i, br in enumerate(brs):
        x1 = x2 + 0.001
        x2 = x1 + round(br*25,1)

        box = ROOT.TBox(x1, y1, x2, y2)
        box.SetFillColor(get_color(colors[i]))
        ROOT.SetOwnership(box, False)
        box.Draw()

def draw_m3mu_frame(m3min, m3max, mumin, mumax, glmin=None, glmax=None, n1min=None, n1max=None):

    canvas = ROOT.TCanvas('', '', 800,800)
    canvas.SetTickx(0)
    canvas.SetTicky(0)

    ROOT.SetOwnership(canvas, False)

    nx = (m3max - m3min) / 25
    ny = (mumax - mumin) / 25

    dx = 25
    dy = 25

    frame = ROOT.TH2F('h2', 'h2', nx, m3min, m3max, ny, mumin, mumax)
    ROOT.SetOwnership(frame, False)
    frame.SetTitle('')

    canvas.SetTicks()
    canvas.SetLeftMargin(0.12)
    canvas.SetBottomMargin(0.121)

    if glmin is not None:
        canvas.SetRightMargin(0.12)
        canvas.SetTopMargin(0.12)

    frame.SetLabelOffset(0.012, "X") # label offset on x axis
    frame.SetLabelOffset(0.012, "Y") # label offset on x axis
    frame.SetXTitle('M_{3} [GeV]')
    frame.SetYTitle('#mu [GeV]')
    frame.GetXaxis().SetTitleSize(0.03)
    frame.GetYaxis().SetTitleSize(0.03)
    frame.GetXaxis().SetLabelSize(0.03)
    frame.GetYaxis().SetLabelSize(0.03)
    frame.GetXaxis().SetTitleOffset(1.4)
    frame.GetYaxis().SetTitleOffset(1.8)

    frame.GetXaxis().SetNdivisions(10, 3, 0)
    frame.GetYaxis().SetNdivisions(10, 5, 0)

    frame.Draw("hist")
    ROOT.gROOT.ForceStyle()

    # hack for GGM . The physics limit is not in M3-mu but in m_gl-m_chi10. So transform one into the other!
    if glmax is not None:
        m = float(glmax-glmin)/(m3max-m3min)
        y0 = glmin - m * m3min
        f = '%f+%f*x' % (y0, m)

        #f_m3mg = ROOT.TF1("f_m3mg", "170.511+x*0.896509", 0, 2000)
        f_m3mg = ROOT.TF1("f_m3mg", f, 0, 2500)
        f_m3mg.SetRange(glmin, glmax)

        m = float(n1max-n1min)/(mumax-mumin)
        y0 = n1min - m * mumin
        f = '%f+%f*x' % (y0, m)

        # f_mumn = ROOT.TF1("f_mumn", "-16.9058+x*1.01732", 0, 2000)
        f_mumn = ROOT.TF1("f_mumn", f, 0, 2500)
        f_mumn.SetRange(mumin, mumax)

        xc = min(f_m3mg.Eval(m3max), m3max)
        yc = min(f_m3mg.Eval(mumax), mumax)

        lmg = ROOT.TLine(m3min, f_m3mg.Eval(m3min), xc, yc)
        ROOT.SetOwnership(lmg, False)
        lmg.SetLineStyle(2)
        lmg.SetLineColor(1)
        lmg.Draw()

        valText = ROOT.TLatex()
        ROOT.SetOwnership(valText, False)
        #valText.SetNDC()
        valText.SetTextAlign(11)
        valText.SetTextSize(0.035)
        valText.SetTextColor(ROOT.TColor.GetColor("#555555"))
        valText.SetTextAngle(25)
        valText.DrawLatex((m3max+m3min)/2, f_m3mg.Eval((m3max+m3min)/2)+100, "m_{#tilde{g}} < m_{#tilde{#chi}_{1}^{0}}")
        valText.AppendPad()

        ROOT.gPad.SetTicks(0, 0)

        # m_gluino axis
        # mg_axis = ROOT.TGaxis(frame.GetXaxis().GetXmin(), frame.GetYaxis().GetXmax(), frame.GetXaxis().GetXmax(), frame.GetYaxis().GetXmax(), "f_m3mg", 510, "-")
        mg_axis = ROOT.TGaxis(m3min, mumax, m3max, mumax, "f_m3mg", 510, "-")
        ROOT.SetOwnership(mg_axis, False)
        mg_axis.ImportAxisAttributes(frame.GetXaxis())
        mg_axis.SetTitle("m_{#tilde{g}} [GeV]")
        mg_axis.SetTitleOffset(1.2)
        mg_axis.SetLabelOffset(0.001)
        mg_axis.Draw()

        # m_chi10 axis
        # mu_axis = ROOT.TGaxis(frame.GetXaxis().GetXmax(), frame.GetYaxis().GetXmin(), frame.GetXaxis().GetXmax(), frame.GetYaxis().GetXmax(), "f_mumn", 510, "+L")
        mu_axis = ROOT.TGaxis(m3max, mumin, m3max, mumax, "f_mumn", 510, "+L")
        ROOT.SetOwnership(mu_axis, False)
        mu_axis.ImportAxisAttributes(frame.GetYaxis())
        mu_axis.SetTitle("m_{#tilde{#chi}^{0}_{1}} [GeV]")
        mu_axis.SetLabelOffset(0.01)
        mu_axis.SetTitleOffset(2)
        mu_axis.Draw()

    # Redraw axis and update canvas
    canvas.RedrawAxis()

    return canvas
