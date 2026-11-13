"""
Central data structure for Knit Textile Industry Machineries & Workflows.
Populate the `flowchart_steps` and `machineries` lists within each sub-section
as detailed machinery data becomes available.
Set `"image"` to a local file path (e.g., `"assets/machines/bale_plucker.jpg"`) or URL when ready.
"""

WORKFLOW_DATA = {
    "Spinning": {
        "icon": "🧶",
        "description": "Conversion of raw staple fibers and filaments into high-quality knitting yarns across Rieter's 8 specialized spinning and yarn processing systems.",
        "subsections": {
            "Fiber preparation machines": {
                "description": "Blowroom and carding technology — engineered for efficient fiber utilization, gentle opening, cleaning, blending, and superior carded sliver quality.",
                "flowchart_steps": [
                    "Bale Opening (UNIfloc A 12)",
                    "Pre-Cleaning (UNIclean B 12 / B 15)",
                    "Homogeneous / Multi-Component Blending (UNImix B 72/B 76 · UNIblend A 81)",
                    "Fine Cleaning & Opening (UNIstore A 79 · UNIclean B 17)",
                    "Foreign Matter Extraction & Air Transport (A 49 · Condensers A 21/A 22)",
                    "High-Performance Carding (Card C 81 / Card C 77)"
                ],
                "machineries": [
                    {
                        "step": "Complete Modular Blowroom Line",
                        "machine_name": "Blowroom Line VARIOline & VARIOline ECOrized",
                        "input": "Raw Cotton, Man-Made, or Recycled Fiber Bales",
                        "output": "Opened, Cleaned & Blended Microtuft Flow to Cards",
                        "purpose": "Variable blowroom concept delivering up to 2,400 kg/h output with 40% lower energy use and 1% raw material savings; VARIOline ECOrized cuts fiber transport energy by an additional 30%.",
                        "image": None
                    },
                    {
                        "step": "Bale Opening",
                        "machine_name": "Automatic Bale Opener UNIfloc A 12",
                        "input": "Compressed Fiber Bales (Assortment Laydown)",
                        "output": "Uniform Microtufts",
                        "purpose": "Opens compressed fiber bales gently into uniform microtufts at up to 2,400 kg/h output for optimal downstream cleaning and blending.",
                        "image": None
                    },
                    {
                        "step": "Pre-Cleaning",
                        "machine_name": "Pre-Cleaner UNIclean B 15 / UNIclean B 12",
                        "input": "Opened Fiber Microtufts",
                        "output": "Pre-Cleaned & Dedusted Fiber Tufts",
                        "purpose": "Performs gentle, uninhibited pre-cleaning and dedusting immediately after bale opening without nipping fibers, at high production rates.",
                        "image": None
                    },
                    {
                        "step": "Homogeneous Mixing",
                        "machine_name": "Mixer UNImix B 72 / B 76",
                        "input": "Pre-Cleaned Fiber Stream",
                        "output": "Homogeneously Mixed Fiber Tufts",
                        "purpose": "Uses a 3-point mixing process in 6 or 8 chambers to ensure long-term homogeneity and rapid adjustment to different raw materials.",
                        "image": None
                    },
                    {
                        "step": "Precision Multi-Component Blending",
                        "machine_name": "Precision Blender UNIblend A 81",
                        "input": "2 to 4 Different Fiber Components (Cotton, Synthetics, Dyed, Recycled)",
                        "output": "Accurately Proportioned Multi-Component Fiber Blend",
                        "purpose": "Delivers high-precision multi-component blending (deviation under 1%) for melange, blended, and recycled knitting yarns.",
                        "image": None
                    },
                    {
                        "step": "Fine Opening & Cleaning",
                        "machine_name": "UNIstore A 79 & Fine Cleaner UNIclean B 17",
                        "input": "Blended Fiber Tufts",
                        "output": "Finely Opened & Cleaned Micro-Flocks",
                        "purpose": "Combines storage/feeding (UNIstore A 79) with intensive fine trash and seed-coat fragment removal (UNIclean B 17) for natural fibers with high trash content.",
                        "image": None
                    },
                    {
                        "step": "Small-Assortment Mixing & Waste Recovery",
                        "machine_name": "Mixing Opener B 33 / Mixing Bale Opener B 34 & Waste Opener B 25",
                        "input": "Small Fiber Lots or Roving/Sliver Waste",
                        "output": "Opened & Reusable Fiber Flocks",
                        "purpose": "Provides compact mixing and opening for small assortments (B 33 / B 34) and economical recovery of spinning waste (B 25).",
                        "image": None
                    },
                    {
                        "step": "Material Transport, Protection & Control",
                        "machine_name": "Condensers A 21 / A 22, Solid Matter Extractor A 49 & UNIcontrol",
                        "input": "Pneumatically Conveyed Fiber Stream",
                        "output": "Protected, Constant Chute-Feed Batt Flow",
                        "purpose": "Separates transport air (A 21/A 22), extracts heavy foreign parts/sparks for system safety (A 49), and maintains continuous material flow from blowroom to cards (UNIcontrol).",
                        "image": None
                    },
                    {
                        "step": "High-Output Carding",
                        "machine_name": "Card C 81",
                        "input": "Blowroom Chute-Fed Fiber Batt",
                        "output": "Carded Sliver (up to 40% Higher Output)",
                        "purpose": "Market-leading energy-efficient card featuring the largest active carding area, intelligent Carding Gap Control (CGC), and Integrated Grinding System (IGS) for maximum sliver quality and fiber yield.",
                        "image": None
                    },
                    {
                        "step": "Economical High-Production Carding",
                        "machine_name": "Card C 77",
                        "input": "Blowroom Chute-Fed Fiber Batt",
                        "output": "Uniform Carded Sliver",
                        "purpose": "Delivers high production of outstanding carded sliver quality with energy savings of up to 30% across cotton, man-made fibers, and blends.",
                        "image": None
                    }
                ]
            },
            "Spinning preparation machines": {
                "description": "Draw frames, combers, and roving frames delivering superior sliver evenness, optimal short-fiber removal, and uniform roving bobbins.",
                "flowchart_steps": [
                    "Breaker Drawing (Draw Frame SB-D 55 / SB-D 27)",
                    "Combing Preparation / Lap Forming (OMEGAlap E 40 / E 36)",
                    "Combing (Comber E 90 / Comber E 86)",
                    "Finisher Autoleveler Drawing (RSB-D 55 / RSB-D 27 / RSB-Module 55)",
                    "Roving Preparation (Roving Frame F 40 / F 20 / F 37)"
                ],
                "machineries": [
                    {
                        "step": "Single-Head Breaker & Autoleveler Drawing",
                        "machine_name": "Autoleveler Draw Frame RSB-D 55 & Draw Frame SB-D 55",
                        "input": "6–8 Carded or Combed Slivers",
                        "output": "Highly Parallelized, Autoleveled Drawn Sliver",
                        "purpose": "Single-head draw frames offering scanning precision, superior sliver evenness, and delivery speeds up to 1,200 m/min (RSB-D 55 with autoleveling; SB-D 55 without autoleveling).",
                        "image": None
                    },
                    {
                        "step": "Double-Head Breaker & Autoleveler Drawing",
                        "machine_name": "Autoleveler Draw Frame RSB-D 27 & Draw Frame SB-D 27",
                        "input": "Carded or Combed Sliver Cans (Dual Delivery)",
                        "output": "2 Parallel Drawn Slivers in Cans",
                        "purpose": "Space-saving double-head draw frames delivering up to 1,200 m/min per delivery with precise autoleveling (RSB-D 27) or non-autoleveled pre-drawing (SB-D 27).",
                        "image": None
                    },
                    {
                        "step": "Direct Card-to-Draw-Frame Coupling",
                        "machine_name": "Autoleveler Draw Frame Module RSB-Module 55",
                        "input": "Direct Sliver Feed from Card C 81",
                        "output": "Autoleveled Drawn Sliver",
                        "purpose": "Directly connects the card with an autoleveler draw frame module to reduce draw frame passages and boost mill efficiency.",
                        "image": None
                    },
                    {
                        "step": "Combing Preparation (Lap Winding)",
                        "machine_name": "Combing Preparation OMEGAlap E 40 / OMEGAlap E 36",
                        "input": "24–28 Pre-Drawn Slivers",
                        "output": "Uniformly Wound Comber Laps",
                        "purpose": "Uses belt-winding technology to produce uniform laps at up to 800 kg/h output (OMEGAlap E 40) with fast lap change and low energy consumption.",
                        "image": None
                    },
                    {
                        "step": "High-Productivity Combing",
                        "machine_name": "Comber E 90",
                        "input": "8 Comber Laps from OMEGAlap",
                        "output": "Combed Sliver (Short Fibers & Neps Removed)",
                        "purpose": "Achieves up to 600 nips/min and over 100 kg/h combed sliver output with raw material savings and consistent quality for fine knitwear yarns.",
                        "image": None
                    },
                    {
                        "step": "Automated Precision Combing",
                        "machine_name": "Comber E 86",
                        "input": "8 Comber Laps from OMEGAlap",
                        "output": "Premium Combed Sliver",
                        "purpose": "Features the largest active combing area (90° combing cylinder) and full ROBOlap automation for top efficiency and flexible noil extraction.",
                        "image": None
                    },
                    {
                        "step": "Automated / Semi-Automated Roving",
                        "machine_name": "Roving Frame F 40 / F 20",
                        "input": "Finisher Drawn Sliver Cans",
                        "output": "Twisted Roving Bobbins",
                        "purpose": "Attenuates drawn sliver and winds uniform roving bobbins with up to 252 spindles and fast doffing (fully automated on F 40; semi-automated on F 20).",
                        "image": None
                    },
                    {
                        "step": "Compact Fully Automatic Roving",
                        "machine_name": "Fully Automatic Roving Frame F 37",
                        "input": "Finisher Drawn Sliver Cans",
                        "output": "Roving Bobbins Ready for Ring/Compact Spinning",
                        "purpose": "Combines up to 220 spindles, compact design, electronic drafting, and automated doffing for consistent roving quality.",
                        "image": None
                    }
                ]
            },
            "Ring spinning machines": {
                "description": "Efficient ring-spinning machines delivering high-quality Com4ring yarns with flexible configurations, high spindle speeds, and energy-saving design.",
                "flowchart_steps": [
                    "Roving Bobbin Creeling / SERVOtrail Transport",
                    "3-Roller Double-Apron Drafting",
                    "Ring & Traveler Twist Insertion (Short-Balloon / High-Speed Package)",
                    "Individual Spindle Monitoring (ISM) & ROBOspin Piecing",
                    "Automatic Cop Doffing & Link to Winding"
                ],
                "machineries": [
                    {
                        "step": "Ring Yarn Spinning",
                        "machine_name": "Ring Spinning Machine G 38",
                        "input": "Roving Bobbins (plus Optional Core Filament / Fancy Slub Feed)",
                        "output": "Com4ring Spun Yarn Cops (Standard, Compact, or Core/Twin/Fancy Yarns)",
                        "purpose": "Flagship ring spinning machine with up to 1,824 spindles, electronic drafting drive, integrated ISM premium monitoring, automatic doffing, and energy-efficient design.",
                        "image": None
                    },
                    {
                        "step": "High-Speed Spindle & Ring Configuration",
                        "machine_name": "High-Speed Package & Short-Balloon Setting",
                        "input": "Drafted Fiber Strand on Ring Frame",
                        "output": "High-Speed Spun Ring Cops with Reduced Ends-Down",
                        "purpose": "Coordinates optimized spindles, Ri-Q-Tubes, and rings/travelers with short-balloon geometry to boost productivity by up to 12% and reduce yarn breaks by 10%.",
                        "image": None
                    },
                    {
                        "step": "Automated Piecing & Roving Transport",
                        "machine_name": "ROBOspin Piecing Robot & SERVOtrail Roving Transport",
                        "input": "Roving Bobbins & Ring Spinning Spindles",
                        "output": "Continuously Pieced & Automatically Creel-Fed Ring Spindles",
                        "purpose": "Automates bobbin transport from roving frame to ring frame and autonomously repairs yarn breaks 24/7 to reduce operator workload.",
                        "image": None
                    }
                ]
            },
            "Compact-spinning machines": {
                "description": "Versatile compact-spinning machines and compacting devices enabling premium Com4compact yarn production with full fiber integration, low hairiness, and high tenacity.",
                "flowchart_steps": [
                    "Roving Feeding",
                    "Main Drafting Zone Attenuation",
                    "Pneumatic / Mechanical Fiber Compacting Zone",
                    "Twist Insertion & Cop Winding",
                    "Automated Cop Doffing"
                ],
                "machineries": [
                    {
                        "step": "High-Speed Compact Yarn Spinning",
                        "machine_name": "Compact-Spinning Machine K 48",
                        "input": "Carded or Combed Roving Bobbins",
                        "output": "Low-Hairiness, High-Strength Com4compact Yarn Cops",
                        "purpose": "Dedicated compact-spinning machine (up to 1,824 spindles) with perforated drum compacting, 18% lower energy consumption, ISM monitoring, and fast 90-second doffing.",
                        "image": None
                    },
                    {
                        "step": "Universal Magnetic/Pneumatic Compacting",
                        "machine_name": "Compacting Solution COMPACT4",
                        "input": "Drafted Fiber Strand on Ring Spinning Frame",
                        "output": "Uniformly Compacted Yarn Strand",
                        "purpose": "Universal four-roller compacting unit mounted on ring spinning machines to deliver consistently high compact yarn quality across carded, combed, and recycled fibers.",
                        "image": None
                    },
                    {
                        "step": "3D Apron Suction Compacting",
                        "machine_name": "Compacting Device COMPACTapron",
                        "input": "Drafted Fiber Strand",
                        "output": "Fine & Extra-Fine Compact Yarn (up to Ne 100+)",
                        "purpose": "Uses a 3D suction guide beneath a mesh apron to transport fibers directly to the nip line with 22% lower energy use and minimal maintenance.",
                        "image": None
                    },
                    {
                        "step": "Mechanical Double-Compacting",
                        "machine_name": "Mechanical Compacting System COMPACTeasy",
                        "input": "Drafted Fiber Strand",
                        "output": "Compacted Ring Yarn with Zero Additional Suction Energy",
                        "purpose": "Y-shaped mechanical dual-channel condenser that reduces hairiness by ~10% and increases yarn strength by ~5% without requiring external vacuum power.",
                        "image": None
                    },
                    {
                        "step": "Removable Drum Compacting",
                        "machine_name": "Compacting Device COMPACTdrum",
                        "input": "Drafted Fiber Strand",
                        "output": "Compact Yarn or Conventional Ring Yarn (Quick Switch)",
                        "purpose": "Flexible perforated-drum compacting device allowing rapid switching between standard ring yarn and compact yarn on the same machine.",
                        "image": None
                    }
                ]
            },
            "Rotor spinning machines": {
                "description": "Automatic and semi-automatic open-end rotor spinning machines combining high productivity, flexibility, and automation to spin sliver directly into cross-wound packages.",
                "flowchart_steps": [
                    "Drawn Sliver Can Feeding",
                    "Fiber Opening by Opening Roller & Trash Extraction",
                    "Fiber Transport & Condensation in High-Speed Rotor Groove",
                    "Open-End Twist Insertion & Yarn Clearer Q 30 Inspection",
                    "Direct Cross-Wound Package Winding & Automatic Doffing"
                ],
                "machineries": [
                    {
                        "step": "Fully Automated Open-End Rotor Spinning",
                        "machine_name": "Rotor Spinning Machine R 70",
                        "input": "Drawn Sliver Cans (Virgin, Blended, or Recycled Fibers)",
                        "output": "Waxed Cross-Wound Com4rotor Yarn Cones / Packages",
                        "purpose": "Fully automated rotor spinning machine with autonomous spinboxes, individual drive technology, Yarn Clearer Q 30, and continuous VARIOlot change—delivering 7% higher output and minimal energy use.",
                        "image": None
                    },
                    {
                        "step": "Semi-Automated Open-End Rotor Spinning",
                        "machine_name": "Semi-Automated Rotor Spinning Machine R 37 (with Optional ROBOdoff)",
                        "input": "Drawn Sliver Cans (Cotton, Polyester, or High-Recycled Content)",
                        "output": "Cross-Wound Rotor Yarn Packages",
                        "purpose": "Economical double-sided rotor spinning machine (up to 600 rotors) with AMIspin electronic piecing, independent machine sides, and optional ROBOdoff automatic package doffing.",
                        "image": None
                    }
                ]
            },
            "Air-jet spinning machines": {
                "description": "Future-ready air-jet spinning technology using compressed air vortex twist to spin drawn sliver directly into pill-resistant Com4jet yarn packages at up to 600 m/min.",
                "flowchart_steps": [
                    "Drawn Sliver Can Feeding",
                    "4-Roller High-Speed Drafting",
                    "Compressed-Air Vortex Twist Insertion (Air-Jet Spinbox)",
                    "Optical Yarn Clearing (Yarn Clearer Q 30)",
                    "Precision Package Winding & Robot Doffing"
                ],
                "machineries": [
                    {
                        "step": "High-Speed Air-Jet Spinning",
                        "machine_name": "Air-Jet Spinning Machine J 70",
                        "input": "Finisher Drawn Sliver Cans (Viscose, Modal, Polyester, Carded/Combed Cotton & Blends)",
                        "output": "Cross-Wound Com4jet Yarn Packages (Ready for Knitting)",
                        "purpose": "Double-sided air-jet spinning machine with 200 autonomous spinning units, 4 multi-tasking robots, Yarn Clearer Q 30, and delivery speeds up to 600 m/min—producing low-pilling, smooth knitting yarns.",
                        "image": None
                    }
                ]
            },
            "Winding machines": {
                "description": "Advanced automatic package winders and SSM yarn processing solutions for clearing yarn faults, splicing, waxing, and building precision knitting cones.",
                "flowchart_steps": [
                    "Ring / Compact Cop Feeding (Magazine or Direct Link)",
                    "Electronic Yarn Fault Clearing",
                    "Pneumatic / Thermo / Injection Splicing (Smartsplicer)",
                    "Paraffin Waxing for Knitting",
                    "PreciFX / Drum Package Winding & Automatic Cone Doffing"
                ],
                "machineries": [
                    {
                        "step": "Automatic Cone Winding & Clearing",
                        "machine_name": "Winding Machine Autoconer X6",
                        "input": "Ring or Compact Spun Yarn Cops",
                        "output": "Cleared, Spliced & Waxed Knitting Cones / Dye Packages",
                        "purpose": "Flagship automatic package winder (up to 96 winding units) featuring Smartjet upper-yarn search, Smartsplicer / Thermosplicer technology, RFID bobbin tracking, and PreciFX digital package build.",
                        "image": None
                    },
                    {
                        "step": "Precision Assembly Winding",
                        "machine_name": "SSM Precision Assembly Winder (NEO-BD)",
                        "input": "2 or More Single-Ply Yarn Cones",
                        "output": "Doubled Multi-Ply Assembly Wound Packages",
                        "purpose": "Doubles multiple yarn ends with balanced tension, high package density, and knot-free lengths ready for two-for-one twisting.",
                        "image": None
                    },
                    {
                        "step": "Specialty Filament & Yarn Processing",
                        "machine_name": "SSM Yarn Processing & Precision Winding Solutions",
                        "input": "Staple-Fiber or Continuous Filament Yarns",
                        "output": "Air-Covered, Drawn, or Soft-Wound Dye Packages",
                        "purpose": "Covers air-covering, filament drawing, and precision dye-package winding for elastic and technical knitwear applications.",
                        "image": None
                    }
                ]
            },
            "Texturing machines": {
                "description": "SSM false-twist and air texturing machines that impart bulk, crimp, elasticity, and a natural spun-fiber look and hand-feel to continuous filament yarns.",
                "flowchart_steps": [
                    "Continuous Filament Supply Creeling (POY / FDY)",
                    "Sequential or Simultaneous Drawing & Thermal Heating Zone",
                    "Texturing (Air-Jet Interlacing for ATY or False-Twist Spindle for DTY)",
                    "Thermal Stabilization / Heat-Setting",
                    "Precision Package Take-Up Winding"
                ],
                "machineries": [
                    {
                        "step": "Air Texturing (ATY Production)",
                        "machine_name": "SSM Air Texturing Machines",
                        "input": "Flat Continuous Filament Yarns (Polyester, Polyamide, Polypropylene)",
                        "output": "Air-Textured Yarn (ATY) Packages with Spun-Fiber Hand-Feel",
                        "purpose": "Uses compressed air jets to entangle and loop continuous filaments, giving synthetic yarns a natural cotton-like appearance and soft touch for activewear and knit fabrics.",
                        "image": None
                    },
                    {
                        "step": "False-Twist Texturing (DTY Production)",
                        "machine_name": "SSM False-Twist Texturing Machines",
                        "input": "Partially Oriented Yarn (POY) / Flat Filament Packages",
                        "output": "Draw-Textured Yarn (DTY) Cones with High Stretch & Bulk",
                        "purpose": "Applies simultaneous drawing, heating, and false-twist crimping along optimized yarn paths to produce elastic, bulky DTY yarns for circular and seamless knitting.",
                        "image": None
                    }
                ]
            }
        }
    },
    "Knitting": {
        "icon": "🪡",
        "description": "Intermeshing yarn loops to produce tubular or open-width knit fabrics and flat knit panels.",
        "subsections": {
            "Circular Knitting": {
                "description": "High-speed production of continuous tubular or open-width knit fabrics (Single Jersey, Rib, Interlock, Fleece).",
                "flowchart_steps": [
                    "Yarn Cone Creeling",
                    "Positive Yarn Feeding",
                    "Circular Loop Formation",
                    "Fabric Take-Down & Winding / Folding",
                    "Greige Fabric Inspection"
                ],
                "machineries": [
                    {
                        "step": "Circular Loop Formation (Single Knit)",
                        "machine_name": "Single Jersey Circular Knitting Machine (Placeholder)",
                        "input": "Spun Yarn Cones & Lycra/Elastane",
                        "output": "Greige Single Jersey / Pique / Fleece Roll",
                        "purpose": "Knits single-bed structures using cylinder needles and sinkers.",
                        "image": None
                    },
                    {
                        "step": "Circular Loop Formation (Double Knit)",
                        "machine_name": "Double Jersey (Rib / Interlock) Machine (Placeholder)",
                        "input": "Spun Yarn Cones",
                        "output": "Greige Rib / Interlock Fabric Roll",
                        "purpose": "Knits double-bed structures using both cylinder and dial needles.",
                        "image": None
                    },
                    {
                        "step": "Greige Fabric Inspection",
                        "machine_name": "Greige Fabric Inspection Machine (Placeholder)",
                        "input": "Knitted Greige Roll",
                        "output": "Inspected & Graded Greige Batch",
                        "purpose": "Detects knitting faults (needle lines, drop stitches, oil spots) under 4-point system.",
                        "image": None
                    }
                ]
            },
            "Flat Knitting": {
                "description": "Production of flat-bed knitted trimmings (collars, cuffs) and shaped sweater panels.",
                "flowchart_steps": [
                    "CAD Pattern Programming",
                    "Yarn Creeling",
                    "V-Bed / Flat Knitting",
                    "Panel Steaming & Relaxation"
                ],
                "machineries": [
                    {
                        "step": "V-Bed / Flat Knitting",
                        "machine_name": "Computerized Jacquard Flat Knitting Machine (Placeholder)",
                        "input": "Dyed or Greige Yarn Cones",
                        "output": "Knitted Collars, Cuffs, or Sweater Panels",
                        "purpose": "Produces semi-fashioned panels or rib trims with bidirectional carriage strokes.",
                        "image": None
                    },
                    {
                        "step": "Panel Steaming & Relaxation",
                        "machine_name": "Flat Knit Steam Ironing Table (Placeholder)",
                        "input": "Raw Flat-Knitted Panels / Collars",
                        "output": "Dimensionally Relaxed Panels",
                        "purpose": "Relaxes loop tension and stabilizes dimensions via steam.",
                        "image": None
                    }
                ]
            }
        }
    },
    "Dyeing": {
        "icon": "🧪",
        "description": "Wet processing, pretreatment, coloration, and finishing of fibers, yarns, and knitted fabrics.",
        "subsections": {
            "Fabric Dyeing": {
                "description": "Pretreatment (scouring/bleaching), coloration, dewatering, drying, and compaction of knit fabrics.",
                "flowchart_steps": [
                    "Batching & Turn-Turning",
                    "Scouring, Bleaching & Exhaust Dyeing",
                    "Slitting & Dewatering",
                    "Drying / Stentering",
                    "Compacting"
                ],
                "machineries": [
                    {
                        "step": "Scouring, Bleaching & Exhaust Dyeing",
                        "machine_name": "Soft-Flow / Winch / Jet Fabric Dyeing Machine (Placeholder)",
                        "input": "Greige Knit Fabric Batch + Dyes & Auxiliaries",
                        "output": "Wet Dyed Rope Fabric",
                        "purpose": "Scours, bleaches, and dyes knit fabric in rope form with low tension.",
                        "image": None
                    },
                    {
                        "step": "Slitting & Dewatering",
                        "machine_name": "Rope Opener & Slitting / Hydro-Extractor Machine (Placeholder)",
                        "input": "Wet Dyed Tubular Fabric",
                        "output": "Dewatered Open-Width / Tubular Fabric",
                        "purpose": "Untwists rope, slits tubular fabric (if open-width), and removes excess water.",
                        "image": None
                    },
                    {
                        "step": "Drying / Stentering",
                        "machine_name": "Stenter Frame / Relax Dryer (Placeholder)",
                        "input": "Wet Dewatered Fabric + Softeners",
                        "output": "Dried & Width-Set Knit Fabric",
                        "purpose": "Dries fabric, applies chemical finishes, and controls GSM and width via overfeed.",
                        "image": None
                    },
                    {
                        "step": "Compacting",
                        "machine_name": "Open-Width / Tubular Compactor (Placeholder)",
                        "input": "Dried Knit Fabric",
                        "output": "Finished Dimensionally Stable Fabric Roll",
                        "purpose": "Controls residual shrinkage and imparts smooth hand-feel via felt/shoe calendering.",
                        "image": None
                    }
                ]
            },
            "Yarn Dyeing": {
                "description": "Package dyeing of yarn cones for feeder/auto-stripe knits, yarn-dyed jacquards, and flat knits.",
                "flowchart_steps": [
                    "Soft Winding (Perforated Cheese)",
                    "Package Loading & Carrier Insertion",
                    "High-Temperature Package Dyeing",
                    "Centrifugal Hydro-Extraction",
                    "RF / Cabinet Drying",
                    "Hard Re-Winding (Precision Cone)"
                ],
                "machineries": [
                    {
                        "step": "Soft Winding (Perforated Cheese)",
                        "machine_name": "Precision Soft Package Winder (Placeholder)",
                        "input": "Greige Ring Yarn Cones",
                        "output": "Low-Density Perforated Dye Packages",
                        "purpose": "Winds yarn at uniform low density onto perforated springs/tubes for liquor penetration.",
                        "image": None
                    },
                    {
                        "step": "High-Temperature Package Dyeing",
                        "machine_name": "HTHP Package Dyeing Machine (Placeholder)",
                        "input": "Soft Yarn Packages + Dye Liquor",
                        "output": "Wet Dyed Yarn Packages",
                        "purpose": "Circulates dye liquor inside-out and outside-in through yarn packages under pressure.",
                        "image": None
                    },
                    {
                        "step": "RF / Cabinet Drying",
                        "machine_name": "Radio Frequency (RF) Dryer (Placeholder)",
                        "input": "Hydro-Extracted Dyed Packages",
                        "output": "Uniformly Dried Yarn Packages",
                        "purpose": "Evaporates residual moisture uniformly without over-drying outer yarn layers.",
                        "image": None
                    }
                ]
            },
            "Fiber Dyeing": {
                "description": "Stock dyeing of loose fibers prior to spinning to produce heather and melange yarns.",
                "flowchart_steps": [
                    "Bale Opening",
                    "Fiber Cake Stamping / Loading",
                    "Loose Stock Dyeing",
                    "Centrifugal Hydro-Extraction",
                    "Conveyor Fiber Drying",
                    "Bale Packing for Spinning"
                ],
                "machineries": [
                    {
                        "step": "Loose Stock Dyeing",
                        "machine_name": "HTHP Loose Fiber / Stock Dyeing Machine (Placeholder)",
                        "input": "Compressed Loose Fiber Cake + Dyes",
                        "output": "Wet Dyed Fiber Mass",
                        "purpose": "Pumps dye liquor through packed loose fiber cages for melange yarn production.",
                        "image": None
                    },
                    {
                        "step": "Conveyor Fiber Drying",
                        "machine_name": "Perforated Drum / Conveyor Dryer (Placeholder)",
                        "input": "Hydro-Extracted Dyed Fibers",
                        "output": "Dried Dyed Loose Fibers",
                        "purpose": "Opens wet fiber cakes and dries them continuously via hot air circulation.",
                        "image": None
                    }
                ]
            }
        }
    },
    "Garments": {
        "icon": "👕",
        "description": "Conversion of finished knitted fabrics into ready-made knit garments including embellishments.",
        "subsections": {
            "Cutting": {
                "description": "Receiving graded patterns and cutting ratios, marker making, fabric checking, tensionless spreading, precision cutting, numbering, bundling, and dispatching cut panels.",
                "flowchart_steps": [
                    "Pattern Received from Pattern Department",
                    "Cutting Ratio Received from Merchandiser",
                    "Marker Making",
                    "Fabric Received from Store",
                    "Fabric Checking (Shade Variation Check)",
                    "Fabric Spreading (Lay Height & Ply Tension)",
                    "Marker Placing onto the Lay",
                    "Cutting the Fabric",
                    "Numbering",
                    "Checking (Comparing with Marker)",
                    "Sorting and Bundling",
                    "Send to Sewing / Next Department"
                ],
                "machineries": [
                    {
                        "step": "Marker Making",
                        "machine_name": "CAD System & Wide-Format Marker Plotter (Placeholder)",
                        "input": "Digital Garment Pattern & Size Ratio",
                        "output": "Printed Paper Marker / Digital Cut File",
                        "purpose": "Optimizes pattern placement to maximize fabric utilization (marker efficiency).",
                        "image": None
                    },
                    {
                        "step": "Fabric Spreading (Lay Height & Ply Tension)",
                        "machine_name": "Automatic Tensionless Knit Fabric Spreader (Placeholder)",
                        "input": "Finished Knit Fabric Rolls",
                        "output": "Multi-Ply Fabric Lay",
                        "purpose": "Spreads knit fabric plies evenly without tension to prevent dimensional distortion.",
                        "image": None
                    },
                    {
                        "step": "Cutting the Fabric",
                        "machine_name": "Straight Knife / Automatic CNC Cutter & Band Knife (Placeholder)",
                        "input": "Multi-Ply Fabric Lay",
                        "output": "Cut Garment Panels",
                        "purpose": "Cuts fabric lays accurately into front, back, sleeve, and neck-rib components.",
                        "image": None
                    }
                ]
            },
            "Sewing": {
                "description": "End-to-end garment sewing department workflow—from product analysis and line balancing to in-line QC and final inspection—alongside product-specific sewing machine line layouts.",
                "flowchart_steps": [
                    "Product Analysis",
                    "Set Up a Target for Production",
                    "Set Up Machine Layout Based on Target",
                    "Set Up Operator Layout Based on Target",
                    "QC Check of the Product",
                    "Line Balancing",
                    "Line Setup",
                    "Distribution of All the Processes",
                    "Cutting Parts Received Section",
                    "Cutting Parts Distribution to Operator & Helper",
                    "Complete Parts Making Individually",
                    "Online QC Check",
                    "Online Quality Audit",
                    "Counting Output & Checking with Target",
                    "Final Quality Check (For Each Garment)"
                ],
                "product_flowcharts": {
                    "T-Shirt": {
                        "summary": "Standard 13-operation sewing line layout for a knitted crew-neck T-shirt (26 total machines · Target: 200 pcs/hr · Uses 3 machine types: Overlock [O/L: 9], Plain Machine [P/M: 13], and Flatlock [F/L: 4]).",
                        "required_machines": [
                            "4-Thread Overlock Chain Stitch Sewing Machine",
                            "Single Needle Lock Stitch Sewing Machine (Plain Machine)",
                            "Top and Bottom Coverage Chain Stitch Machine (Flat Lock)"
                        ],
                        "steps": [
                            {"operation": "Shoulder Joint", "machine": "Overlock Machine", "qty": 2, "target": "200 pcs/hr"},
                            {"operation": "Neck Joint", "machine": "Overlock Machine", "qty": 2, "target": "200 pcs/hr"},
                            {"operation": "Rib Tack", "machine": "Plain Machine", "qty": 1, "target": "200 pcs/hr"},
                            {"operation": "Main Label Join", "machine": "Plain Machine", "qty": 1, "target": "200 pcs/hr"},
                            {"operation": "Neck Tape Join", "machine": "Plain Machine", "qty": 3, "target": "200 pcs/hr"},
                            {"operation": "Neck Top Sin / Topstitch", "machine": "Plain Machine", "qty": 3, "target": "200 pcs/hr"},
                            {"operation": "Sleeve Hem", "machine": "Flatlock Machine", "qty": 2, "target": "200 pcs/hr"},
                            {"operation": "Sleeve Join", "machine": "Overlock Machine", "qty": 2, "target": "200 pcs/hr"},
                            {"operation": "Care Label Join", "machine": "Plain Machine", "qty": 1, "target": "200 pcs/hr"},
                            {"operation": "Side Seam", "machine": "Overlock Machine", "qty": 3, "target": "200 pcs/hr"},
                            {"operation": "Sleeve Tack", "machine": "Plain Machine", "qty": 2, "target": "200 pcs/hr"},
                            {"operation": "Sleeve Soap Tack", "machine": "Plain Machine", "qty": 2, "target": "200 pcs/hr"},
                            {"operation": "Body Hem", "machine": "Flatlock Machine", "qty": 2, "target": "200 pcs/hr"}
                        ]
                    },
                    "Polo Shirt": {
                        "summary": "Complete 37-operation sewing line layout for a knitted Polo Shirt (37 total machines + 5 Table stations · 40 Operators, 26 Helpers · Uses Plain Machine [P/M: 18], Auto Plain Machine [P/M Auto: 3], Overlock [O/L: 8], Flatlock [F/L: 6], Buttonhole [B/H: 1], and Button Attaching [B/A: 1]).",
                        "required_machines": [
                            "Single Needle Lock Stitch Sewing Machine (Plain Machine)",
                            "Auto Plain Machine (Computerized Single Needle Lock Stitch with Auto-Trimmer)",
                            "4-Thread Overlock Chain Stitch Sewing Machine",
                            "Top and Bottom Coverage Chain Stitch Machine (Flat Lock)",
                            "Button Hole Lock Stitch Sewing Machine",
                            "Button Attaching Sewing Machine"
                        ],
                        "steps": [
                            {"operation": "Placket Rolling", "machine": "Plain Machine (P/M)", "qty": 1},
                            {"operation": "Moon (Back Neck Half-Moon)", "machine": "Plain Machine (P/M)", "qty": 1},
                            {"operation": "Moon Topstitch", "machine": "Flatlock Machine (F/L)", "qty": 1},
                            {"operation": "Neck Closing", "machine": "Plain Machine (P/M)", "qty": 1},
                            {"operation": "Placket Matching with Front", "machine": "Table (Manual Matching)", "qty": None},
                            {"operation": "Placket Attaching with Front", "machine": "Auto Plain Machine (P/M Auto)", "qty": 1},
                            {"operation": "Placket Topstitch", "machine": "Plain Machine (P/M)", "qty": 1},
                            {"operation": "Placket Tuck", "machine": "Plain Machine (P/M)", "qty": 1},
                            {"operation": "Matching (Front & Back Part)", "machine": "Table (Manual Matching)", "qty": None},
                            {"operation": "Shoulder Joint with Shoulder Tape", "machine": "Overlock Machine (O/L)", "qty": 1},
                            {"operation": "Shoulder Topstitch", "machine": "Flatlock Machine (F/L)", "qty": 1},
                            {"operation": "Collar Cut Without Thread", "machine": "Overlock Machine (O/L)", "qty": 1},
                            {"operation": "Collar Tuck with Placket", "machine": "Plain Machine (P/M)", "qty": 1},
                            {"operation": "Collar Joint with the Body", "machine": "Overlock Machine (O/L)", "qty": 1},
                            {"operation": "Neck Piping", "machine": "Flatlock Machine (F/L)", "qty": 1},
                            {"operation": "Main Label Joint", "machine": "Plain Machine (P/M)", "qty": 1},
                            {"operation": "Sleeve Hem (Cuff) Joint with Sleeve", "machine": "Overlock Machine (O/L)", "qty": 1},
                            {"operation": "Collar Back Topstitch", "machine": "Flatlock Machine (F/L)", "qty": 2},
                            {"operation": "Cutting & Matching", "machine": "Table (Manual Station)", "qty": None},
                            {"operation": "Sleeve Joint", "machine": "Overlock Machine (O/L)", "qty": 2},
                            {"operation": "Placket Kasa Mara (Slit Tack)", "machine": "Plain Machine (P/M)", "qty": 1},
                            {"operation": "Placket 1/16 Topstitch", "machine": "Auto Plain Machine (P/M Auto)", "qty": 1},
                            {"operation": "Placket Tuck", "machine": "Plain Machine (P/M)", "qty": 1},
                            {"operation": "Care Label Joint", "machine": "Plain Machine (P/M)", "qty": 1},
                            {"operation": "Placket Box Topstitch", "machine": "Plain Machine (P/M)", "qty": 2},
                            {"operation": "Inspection All Back Process", "machine": "Table (In-Line Inspection)", "qty": None},
                            {"operation": "Bottom Hem", "machine": "Flatlock Machine (F/L)", "qty": 1},
                            {"operation": "Side Seam", "machine": "Overlock Machine (O/L)", "qty": 2},
                            {"operation": "Sideband Twill Tape (Side Vent)", "machine": "Plain Machine (P/M)", "qty": 1},
                            {"operation": "Sideband Tuck", "machine": "Plain Machine (P/M)", "qty": 1},
                            {"operation": "Sideband Topstitch", "machine": "Plain Machine (P/M)", "qty": 2},
                            {"operation": "Sleeve Inside Tuck", "machine": "Plain Machine (P/M)", "qty": 1},
                            {"operation": "Sleeve Outside Topstitch", "machine": "Plain Machine (P/M)", "qty": 1},
                            {"operation": "Sideband Tuck (Reinforcement)", "machine": "Plain Machine (P/M)", "qty": 1},
                            {"operation": "Buttonhole", "machine": "Buttonhole Machine (B/H)", "qty": 1},
                            {"operation": "Button Positioning (Marking)", "machine": "Table (Manual Marking)", "qty": None},
                            {"operation": "Button Attaching", "machine": "Button Attaching Machine (B/A)", "qty": 1}
                        ]
                    }
                },
                "machineries": [
                    {
                        "step": "Blind Hemming (Stitch Class 101)",
                        "machine_name": "Blind Stitch Machine",
                        "input": "Folded Hem Edge (Blazer / Trouser Panels) + 1 Needle Thread",
                        "output": "Invisibly Hemmed Garment Edge",
                        "purpose": "Cylinder-bed machine using 1 curved needle (Stitch Class 101, 3000+ RPM) for invisible hemming on blazers and trousers.",
                        "image": None
                    },
                    {
                        "step": "Collar, Placket, Label & General Seaming (Stitch Class 301)",
                        "machine_name": "Single Needle Lock Stitch Sewing Machine (Plain Machine)",
                        "input": "Cut Garment Panels (Collar, Placket, Neck Tape, Sideband, Labels) + Needle & Bobbin Thread",
                        "output": "Lockstitched Placket, Collar Tuck, Neck Tape & Topstitched Assembly",
                        "purpose": "Flat-bed machine with drop-feed mechanism (1 needle, 4000–5000 RPM) used extensively in T-shirt (rib tack, label join, neck tape join, neck topstitch, sleeve tack) and Polo shirt (placket rolling, moon, neck closing, sideband twill tape & box topstitch) sewing lines.",
                        "image": None
                    },
                    {
                        "step": "Precision Placket Attaching & 1/16 Topstitching (Stitch Class 301)",
                        "machine_name": "Auto Plain Machine (Computerized Single Needle Lock Stitch with Auto-Trimmer)",
                        "input": "Polo Front Panel + Prepared Placket + Needle & Bobbin Thread",
                        "output": "Precision-Attached & 1/16\" Topstitched Polo Placket with Auto-Trimmed Threads",
                        "purpose": "Direct-drive computerized single-needle lockstitch machine with automatic thread trimmer, auto back-tack, and programmable stitch count; used in Polo shirt lines for placket attaching with front and placket 1/16 topstitching.",
                        "image": None
                    },
                    {
                        "step": "Knit Garments Joining (Stitch Class 514)",
                        "machine_name": "4-Thread Overlock Chain Stitch Sewing Machine",
                        "input": "Cut Knit Garment Panels + 4 Threads (2 Needle, 2 Looper)",
                        "output": "Joined Knit Panels with Superimposed Overedge Seam",
                        "purpose": "Flat-bed overlock machine (2 needles, 2 loopers, Stitch Class 514, 3000+ RPM) used primarily for knit garments joining.",
                        "image": None
                    },
                    {
                        "step": "Bottom Hemming & Knit Topstitching",
                        "machine_name": "Top and Bottom Coverage Chain Stitch Machine (Flat Lock)",
                        "input": "Knit Body / T-Shirt Hem Panels + 4 Threads (3 Needle, 1 Looper)",
                        "output": "Flat-Hemmed T-Shirt Bottom & Topstitched Knit Seam",
                        "purpose": "Cylinder-bed Flat Lock machine (2–3 needles, 1 looper, 3000+ RPM, edge neatening seam) for T-shirt bottom hems and knit topstitching.",
                        "image": None
                    },
                    {
                        "step": "Lapped Seaming & Tubular Operations (Stitch Class 401)",
                        "machine_name": "Feed of the Arm Machine",
                        "input": "Garment Side Seam / Back Yoke / Sleeve Panels + 4 Threads",
                        "output": "Lap-Seamed Tubular Sleeve & Side Seam Assembly",
                        "purpose": "Arm-bed machine with lap folder (2 needles, Stitch Class 401, 3000+ RPM, lapped seam) for side seams, back yoke joins, sleeve joins, and flat tubular operations.",
                        "image": None
                    },
                    {
                        "step": "Single Fabric Edge Finishing (Stitch Class 504)",
                        "machine_name": "3-Thread Overlock Machine",
                        "input": "Raw-Edge Fabric Panels + 3 Threads (1 Needle, 2 Looper)",
                        "output": "Edge-Neatened Serpentine Overlocked Panel",
                        "purpose": "Flat-bed machine (1 needle, 2 loopers, Stitch Class 504, 3000+ RPM) used for single fabric edge finishing and neatening.",
                        "image": None
                    },
                    {
                        "step": "Decorative Flat Seaming (Stitch Class 404)",
                        "machine_name": "2-Needle Zig Zag Chain Stitch Sewing Machine",
                        "input": "Garment Panels + 2 Needle & 2 Looper Threads",
                        "output": "Decoratively Zig-Zag Chainstitched Flat Seam",
                        "purpose": "Flat-bed machine (2 needles, 2 loopers, Stitch Class 404, 3000+ RPM, flat seam) used for decorative stitching on garments.",
                        "image": None
                    },
                    {
                        "step": "Pre-Programmed Edge Decoration",
                        "machine_name": "Multi-Thread Chain Stitch Machine",
                        "input": "Garment Fabric Edge + Sewing Thread",
                        "output": "Pattern-Decorated Garment Edge",
                        "purpose": "Uses 1 auto-movable needle with pre-installed software patterns for decorative stitching along fabric edges.",
                        "image": None
                    },
                    {
                        "step": "Buttonholing (Stitch Class 304)",
                        "machine_name": "Button Hole Lock Stitch Sewing Machine",
                        "input": "Garment Placket / Collar Band + 3 Threads",
                        "output": "Slit & Lockstitch-Finished Buttonhole",
                        "purpose": "Raised-bed computerized panel machine (1 needle, 3 threads, Stitch Class 304) that cuts and stitches clean buttonholes on fabric.",
                        "image": None
                    },
                    {
                        "step": "Decorative Lockstitching (Stitch Class 315)",
                        "machine_name": "Zig Zag Lock Stitch Sewing Machine",
                        "input": "Garment Panels / Trims + Lockstitch Thread",
                        "output": "Zig-Zag Lockstitched Decorative Seam",
                        "purpose": "Flat-bed machine (Stitch Class 315) used for decorative zig-zag lockstitching applications.",
                        "image": None
                    },
                    {
                        "step": "Button Fastening (Stitch Class 304)",
                        "machine_name": "Button Attaching Sewing Machine",
                        "input": "Garment Placket + 2-Hole or 4-Hole Buttons + Thread",
                        "output": "Button-Attached Garment Placket",
                        "purpose": "Cylinder-bed machine (1 needle, Stitch Class 304) designed for automatically attaching 2-hole or 4-hole buttons onto fabric.",
                        "image": None
                    },
                    {
                        "step": "Safety-Stitch Panel Joining (Stitch Class 516)",
                        "machine_name": "5-Thread Overlock Sewing Machine",
                        "input": "Garment Panels + 5 Threads (2 Needle, 3 Looper)",
                        "output": "High-Strength Superimposed Safety-Stitched Seam",
                        "purpose": "Uses 2 needles and 3 loopers (Stitch Class 516, superimposed seam) for high-strength garment joining.",
                        "image": None
                    },
                    {
                        "step": "Topstitching & Back Yoke Joining",
                        "machine_name": "2-Needle Chain Stitch Machine",
                        "input": "Garment Yoke & Body Panels + 4 Threads (2 Needle, 2 Looper)",
                        "output": "Parallel Chain-Topstitched Back Yoke / Seam",
                        "purpose": "Flat-bed machine (2 needles, 2 loopers, 4 threads) used for topstitching and back yoke joining.",
                        "image": None
                    },
                    {
                        "step": "Pocket Joining & Parallel Lockstitching (Stitch Class 301)",
                        "machine_name": "2-Needle Lock Stitch Sewing Machine",
                        "input": "Pocket & Garment Body Panels + 2 Needles & 2 Bobbins",
                        "output": "Double-Needle Lockstitched Pocket / Seam",
                        "purpose": "Flat-bed machine (2 needles with single-needle disengagement option, 2 bobbins, Stitch Class 301) used for pocket joining and heavy seams.",
                        "image": None
                    },
                    {
                        "step": "Label & Velcro Fastener Attachment",
                        "machine_name": "Velcro Tape Attach Sewing Machine",
                        "input": "Garment Panel + Brand Label / Velcro Tape + Thread",
                        "output": "Label- or Velcro-Attached Garment Component",
                        "purpose": "Cylinder-bed 1-needle cyclic machine used for attaching labels, Velcro tapes, and decorative patches onto fabric.",
                        "image": None
                    },
                    {
                        "step": "Placket / Box Pleat & Waistband Stitching",
                        "machine_name": "Multi-Thread Multi-Needle Chain Stitch Machine (Kansai)",
                        "input": "Knit or Woven Shirt Front / Waistband + Multi-Thread Cone Creel",
                        "output": "Multi-Row Chainstitched Box Pleat / Placket",
                        "purpose": "Raised-bed Kansai machine (4 to 12 needles, up to 12 loopers / 24 threads) used for sewing shirt box pleats and multi-row elastic/placket seams on knit and woven garments.",
                        "image": None
                    },
                    {
                        "step": "Heavy-Duty Keyhole Buttonholing",
                        "machine_name": "Eyelet Hole Chain Stitch Sewing Machine",
                        "input": "Jacket / Heavy Outerwear Placket + Chainstitch Thread",
                        "output": "Keyhole / Eyelet Buttonhole",
                        "purpose": "Raised-bed specialty machine used to create reinforced eyelet buttonholes on jackets and blazers.",
                        "image": None
                    },
                    {
                        "step": "Interlining Bonding",
                        "machine_name": "Fusing Machine",
                        "input": "Knit/Woven Collar, Placket, or Neck Panels + Fusible Interlining",
                        "output": "Thermally Bonded (Fused) Garment Components",
                        "purpose": "2-roller pressure and heat fusing machine suitable for bonding fusible interlining onto knitted and woven fabric panels.",
                        "image": None
                    }
                ]
            },
            "Printing": {
                "description": "Application of surface graphics and all-over or placement prints onto cut panels or fabrics.",
                "flowchart_steps": [
                    "Artwork Separation & Screen Exposure",
                    "Panel Pallet Loading",
                    "Paste Application / Digital Printing",
                    "Flash Curing (Intermediate)",
                    "Conveyor Heat Curing"
                ],
                "machineries": [
                    {
                        "step": "Paste Application (Chest / Placement Print)",
                        "machine_name": "Automatic Octopus / Oval Screen Printing Machine (Placeholder)",
                        "input": "Cut Garment Panels + Printing Paste & Screens",
                        "output": "Wet Printed Garment Panels",
                        "purpose": "Applies multi-color plastisol, rubber, pigment, or discharge prints with high registration.",
                        "image": None
                    },
                    {
                        "step": "Conveyor Heat Curing",
                        "machine_name": "Gas / IR Conveyor Curing Dryer (Placeholder)",
                        "input": "Wet Printed Garment Panels",
                        "output": "Cured Wash-Fast Printed Panels",
                        "purpose": "Polymerizes and fixes printing ink/paste onto the knit fabric at controlled temperature.",
                        "image": None
                    }
                ]
            },
            "Embroidery": {
                "description": "Decorative thread-based motif stitching on cut garment panels or finished knitwear.",
                "flowchart_steps": [
                    "Embroidery Digitizing (Punching)",
                    "Backing & Framing (Hooping)",
                    "Multi-Head Embroidery Stitching",
                    "Backing Removal & Thread Trimming"
                ],
                "machineries": [
                    {
                        "step": "Multi-Head Embroidery Stitching",
                        "machine_name": "Computerized Multi-Head Embroidery Machine (Placeholder)",
                        "input": "Hooped Garment Panels + Stabilizer Backing + Embroidery Threads",
                        "output": "Embroidered Garment Panels",
                        "purpose": "Stitches multi-color logos, appliques, or sequin motifs simultaneously across multiple heads.",
                        "image": None
                    }
                ]
            }
        }
    }
}
