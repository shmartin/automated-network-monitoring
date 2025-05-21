# sudo mn --custom topo1.py --topo mytopo --controller=remote,ip=127.0.0.1

from mininet.topo import Topo

class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)

        switch_main = self.addSwitch('s1')

        print_main = self.addHost('print_main')
        ntsms_main = self.addHost('ntsms_main')
        touch_main = self.addHost('touch_main')

        self.addLink(print_main, switch_main)
        self.addLink(ntsms_main, switch_main)
        self.addLink(touch_main, switch_main)

        # Server room
        switch_server = self.addSwitch('s2')

        self.addLink(switch_server, switch_main)
        
        smess_srvr = self.addHost('smess_srvr')
        mains_srvr = self.addHost('mains_srvr')
        ipacs_srvr = self.addHost('ipacs_srvr')

        self.addLink(smess_srvr, switch_server)
        self.addLink(mains_srvr, switch_server)
        self.addLink(ipacs_srvr, switch_server)

        # HR Office
        switch_hr = self.addSwitch('s3')

        self.addLink(switch_hr, switch_main)

        rcord_hr = self.addHost('rcord_hr')
        mains_hr = self.addHost('mains_hr')
        payrl_hr = self.addHost('payrl_hr')
        files_hr = self.addHost('files_hr')
        rport_hr = self.addHost('rport_hr')
        accou_hr = self.addHost('accou_hr')

        self.addLink(rcord_hr, switch_hr)
        self.addLink(mains_hr, switch_hr)
        self.addLink(payrl_hr, switch_hr)
        self.addLink(files_hr, switch_hr)
        self.addLink(rport_hr, switch_hr)
        self.addLink(accou_hr, switch_hr)

        # Finance Office
        switch_finance = self.addSwitch('s4')

        self.addLink(switch_finance, switch_main)

        cashi_fnce = self.addHost('cashi_fnce')
        pos___fnce = self.addHost('pos___fnce')
        opd___fnce = self.addHost('opd___fnce')
        er____fnce = self.addHost('er____fnce')
        admit_fnce = self.addHost('admin_fnce')

        self.addLink(cashi_fnce, switch_finance)
        self.addLink(pos___fnce, switch_finance)
        self.addLink(opd___fnce, switch_finance)
        self.addLink(er____fnce, switch_finance)
        self.addLink(admit_fnce, switch_finance)

        # Laboratories
        switch_laboratories = self.addSwitch('s5')

        self.addLink(switch_laboratories, switch_main)

        pharm_labo = self.addHost('pharm_labo')
        cssr__labo = self.addHost('cssr__labo')
        rts___labo = self.addHost('rts___labo')
        radio_labo = self.addHost('radio_labo')
        clini_labo = self.addHost('clini_labo')
        labor_labo = self.addHost('labor_labo')

        self.addLink(pharm_labo, switch_laboratories)
        self.addLink(cssr__labo, switch_laboratories)
        self.addLink(rts___labo, switch_laboratories)
        self.addLink(radio_labo, switch_laboratories)
        self.addLink(clini_labo, switch_laboratories)
        self.addLink(labor_labo, switch_laboratories)

        # Special Units
        switch_special = self.addSwitch('s6')

        rts___spec = self.addHost('rts___fnce')
        icu___spec = self.addHost('icu___fnce')
        or____spec = self.addHost('or____fnce')
        nurse_spec = self.addHost('nurse_fnce')
        stati_spec = self.addHost('stati_fnce')

        self.addLink(rts___spec, switch_special)
        self.addLink(icu___spec, switch_special)
        self.addLink(or____spec, switch_special)
        self.addLink(nurse_spec, switch_special)
        self.addLink(stati_spec, switch_special)

        self.addLink(switch_special, switch_main)

        # Doctor's Clinics
        switch_clinics = self.addSwitch('s7')

        self.addLink(switch_clinics, switch_main)

        h1_clini = self.addHost('h1_clini')
        h2_clini = self.addHost('h2_clini')
        h3_clini = self.addHost('h3_clini')
        h4_clini = self.addHost('h4_clini')
        h5_clini = self.addHost('h5_clini')
        h6_clini = self.addHost('h6_clini')
        h7_clini = self.addHost('h7_clini')
        h8_clini = self.addHost('h8_clini')
        h9_clini = self.addHost('h9_clini')

        self.addLink(h1_clini, switch_clinics)
        self.addLink(h2_clini, switch_clinics)
        self.addLink(h3_clini, switch_clinics)
        self.addLink(h4_clini, switch_clinics)
        self.addLink(h5_clini, switch_clinics)
        self.addLink(h6_clini, switch_clinics)
        self.addLink(h7_clini, switch_clinics)
        self.addLink(h8_clini, switch_clinics)
        self.addLink(h9_clini, switch_clinics)


topos = { 'mytopo': (lambda: MyTopo())}