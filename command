# Vacuum / no compensation
python3 plasma_column_picmi.py --neutralization 0.0 --max_steps 2000

# H2-like compensated column
python3 plasma_column_picmi.py --gas H2 --neutralization 0.90 --max_steps 2000

# Kr-like compensated column
python3 plasma_column_picmi.py --gas Kr --neutralization 0.95 --max_steps 2000



# C++

## 1. First run a parser test: max_steps = 0

### Start with H₂. Generate a base input deck:

python plasma_column_mcc_picmi_v7.py \
    --write_inputs \
    --output_dir runs/cxx_H2_parser \
    --inputs_name inputs_cxx_H2_parser \
    --warpx_data_dir /home/cspark/Work/simulation_codes-working/warpx-data \
    --gas H2 \
    --neutralization 0.0 \
    --pressure_torr 1e-3 \
    --mcc none \
    --max_steps 0 \
    --diag_period 100 \
    --reduced_diag_period 1 \
    --reduced_diag_dir reducedfiles/ \
    --nx 24 --ny 24 --nz 128

cat >> runs/cxx_H2_parser/inputs_cxx_H2_parser <<'EOF'

# ---------------------------------------------------------------------------
# C++ BackgroundMCC ion-impact ionization validation
# Reaction: p + H2 -> p + H2+ + e-
# ---------------------------------------------------------------------------

collisions.collision_names = proton_H2_ioniz

proton_H2_ioniz.type = background_mcc
proton_H2_ioniz.species = beam_protons

# Use high pressure first, 1e-3 torr, to make events easier to observe later.
# 1e-3 torr at 300 K gives ~3.219e19 m^-3.
proton_H2_ioniz.background_density = 3.2188332685e19
proton_H2_ioniz.max_background_density = 3.2188332685e19
proton_H2_ioniz.background_temperature = 300.0
proton_H2_ioniz.background_mass = 3.347e-27

proton_H2_ioniz.scattering_processes = ion_impact_ionization
proton_H2_ioniz.ion_impact_ionization_cross_section = /home/cspark/Work/simulation_codes-working/warpx-data/MCC_cross_sections/H2/proton_impact_ionization.dat
proton_H2_ioniz.ion_impact_ionization_energy = 0.0

proton_H2_ioniz.ion_impact_ionization_electron_species = plasma_electrons
proton_H2_ioniz.ion_impact_ionization_ion_species = gas_ions

proton_H2_ioniz.ion_impact_ionization_electron_energy = 1.0
proton_H2_ioniz.ndt_supercycle = 1
EOF

/home/cspark/Work/simulation_codes-working/warpx/install/bin/warpx.3d \
    inputs_cxx_H2_parser \
    2>&1 | tee ../../logs/cxx_H2_parser.log


## 2. Run a short H₂ C++ MCC validation case

### generate a 2000-step validation deck:

python plasma_column_mcc_picmi_v7.py \
    --write_inputs \
    --output_dir runs/cxx_H2_mcc_2k \
    --inputs_name inputs_cxx_H2_mcc_2k \
    --warpx_data_dir /home/cspark/Work/simulation_codes-working/warpx-data \
    --gas H2 \
    --neutralization 0.0 \
    --pressure_torr 1e-3 \
    --mcc none \
    --max_steps 2000 \
    --diag_period 500 \
    --reduced_diag_period 10 \
    --reduced_diag_dir reducedfiles/ \
    --nx 24 --ny 24 --nz 128

cat >> runs/cxx_H2_mcc_2k/inputs_cxx_H2_mcc_2k <<'EOF'

collisions.collision_names = proton_H2_ioniz

proton_H2_ioniz.type = background_mcc
proton_H2_ioniz.species = beam_protons
proton_H2_ioniz.background_density = 3.2188332685e19
proton_H2_ioniz.max_background_density = 3.2188332685e19
proton_H2_ioniz.background_temperature = 300.0
proton_H2_ioniz.background_mass = 3.347e-27

proton_H2_ioniz.scattering_processes = ion_impact_ionization
proton_H2_ioniz.ion_impact_ionization_cross_section = /home/cspark/Work/simulation_codes-working/warpx-data/MCC_cross_sections/H2/proton_impact_ionization.dat
proton_H2_ioniz.ion_impact_ionization_energy = 0.0
proton_H2_ioniz.ion_impact_ionization_electron_species = plasma_electrons
proton_H2_ioniz.ion_impact_ionization_ion_species = gas_ions
proton_H2_ioniz.ion_impact_ionization_electron_energy = 1.0
proton_H2_ioniz.ndt_supercycle = 1
EOF


/home/cspark/Work/simulation_codes-working/warpx/install/bin/warpx.3d \
    inputs_cxx_H2_mcc_2k \
    2>&1 | tee ../../logs/cxx_H2_mcc_2k.log


## 3. Check whether the C++ MCC process created electrons and ions

ls -lh runs/cxx_H2_mcc_2k/reducedfiles/

python particle_number_diagnostics_v2.py


## 4. Run the Kr C++ MCC validation case

python plasma_column_mcc_picmi_v7.py \
    --write_inputs \
    --output_dir runs/cxx_Kr_mcc_2k \
    --inputs_name inputs_cxx_Kr_mcc_2k \
    --warpx_data_dir /home/cspark/Work/simulation_codes-working/warpx-data \
    --gas Kr \
    --neutralization 0.0 \
    --pressure_torr 1e-3 \
    --mcc none \
    --max_steps 2000 \
    --diag_period 500 \
    --reduced_diag_period 10 \
    --reduced_diag_dir reducedfiles/ \
    --nx 24 --ny 24 --nz 128

cat >> runs/cxx_Kr_mcc_2k/inputs_cxx_Kr_mcc_2k <<'EOF'

collisions.collision_names = proton_Kr_ioniz

proton_Kr_ioniz.type = background_mcc
proton_Kr_ioniz.species = beam_protons

# 1e-3 torr at 300 K.
proton_Kr_ioniz.background_density = 3.2188332685e19
proton_Kr_ioniz.max_background_density = 3.2188332685e19
proton_Kr_ioniz.background_temperature = 300.0
proton_Kr_ioniz.background_mass = 1.391e-25

proton_Kr_ioniz.scattering_processes = ion_impact_ionization
proton_Kr_ioniz.ion_impact_ionization_cross_section = /home/cspark/Work/simulation_codes-working/warpx-data/MCC_cross_sections/Kr/proton_impact_ionization.dat
proton_Kr_ioniz.ion_impact_ionization_energy = 0.0

proton_Kr_ioniz.ion_impact_ionization_electron_species = plasma_electrons
proton_Kr_ioniz.ion_impact_ionization_ion_species = kr_ions

proton_Kr_ioniz.ion_impact_ionization_electron_energy = 1.0
proton_Kr_ioniz.ndt_supercycle = 1
EOF

/home/cspark/Work/simulation_codes-working/warpx/install/bin/warpx.3d \
    inputs_cxx_Kr_mcc_2k \
    2>&1 | tee ../../logs/cxx_Kr_mcc_2k.log


## 5. After validation, run physical pressure

### Once the 1e-3 torr validation works, go back to your physical value:

pressure_torr = 1e-5
background_density = 3.2188332685e17


### For H₂ physical-pressure 20k test:

python plasma_column_mcc_picmi_v7.py \
    --write_inputs \
    --output_dir runs/cxx_H2_mcc_40k_physical \
    --inputs_name inputs_cxx_H2_mcc_40k_physical \
    --warpx_data_dir /home/cspark/Work/simulation_codes-working/warpx-data \
    --gas H2 \
    --neutralization 0.0 \
    --pressure_torr 1e-5 \
    --mcc none \
    --max_steps 40000 \
    --diag_period 5000 \
    --reduced_diag_period 100 \
    --reduced_diag_dir reducedfiles/ \
    --nx 24 --ny 24 --nz 128


cat >> runs/cxx_H2_mcc_40k_physical/inputs_cxx_H2_mcc_40k_physical <<'EOF'

collisions.collision_names = proton_H2_ioniz

proton_H2_ioniz.type = background_mcc
proton_H2_ioniz.species = beam_protons
proton_H2_ioniz.background_density = 3.2188332685e17
proton_H2_ioniz.max_background_density = 3.2188332685e17
proton_H2_ioniz.background_temperature = 300.0
proton_H2_ioniz.background_mass = 3.347e-27

proton_H2_ioniz.scattering_processes = ion_impact_ionization
proton_H2_ioniz.ion_impact_ionization_cross_section = /home/cspark/Work/simulation_codes-working/warpx-data/MCC_cross_sections/H2/proton_impact_ionization.dat
proton_H2_ioniz.ion_impact_ionization_energy = 0.0
proton_H2_ioniz.ion_impact_ionization_electron_species = plasma_electrons
proton_H2_ioniz.ion_impact_ionization_ion_species = gas_ions
proton_H2_ioniz.ion_impact_ionization_electron_energy = 1.0
proton_H2_ioniz.ndt_supercycle = 1
EOF

### Kr for 20k

python plasma_column_mcc_picmi_v7.py \
    --write_inputs \
    --output_dir runs/cxx_Kr_mcc_40k_physical \
    --inputs_name inputs_cxx_Kr_mcc_40k_physical \
    --warpx_data_dir /home/cspark/Work/simulation_codes-working/warpx-data \
    --gas Kr \
    --neutralization 0.0 \
    --pressure_torr 1e-5 \
    --mcc none \
    --max_steps 40000 \
    --diag_period 5000 \
    --reduced_diag_period 100 \
    --reduced_diag_dir reducedfiles/ \
    --nx 24 --ny 24 --nz 128

cat >> runs/cxx_Kr_mcc_40k_physical/inputs_cxx_Kr_mcc_40k_physical <<'EOF'
    
collisions.collision_names = proton_Kr_ioniz
    
proton_Kr_ioniz.type = background_mcc
proton_Kr_ioniz.species = beam_protons

# 1e-3 torr at 300 K.
proton_Kr_ioniz.background_density = 3.2188332685e17
proton_Kr_ioniz.max_background_density = 3.2188332685e17
proton_Kr_ioniz.background_temperature = 300.0
proton_Kr_ioniz.background_mass = 1.391e-25

proton_Kr_ioniz.scattering_processes = ion_impact_ionization
proton_Kr_ioniz.ion_impact_ionization_cross_section = /home/cspark/Work/simulation_codes-working/warpx-data/MCC_cross_sections/Kr/proton_impact_ionization.dat
proton_Kr_ioniz.ion_impact_ionization_energy = 0.0

proton_Kr_ioniz.ion_impact_ionization_electron_species = plasma_electrons
proton_Kr_ioniz.ion_impact_ionization_ion_species = kr_ions

proton_Kr_ioniz.ion_impact_ionization_electron_energy = 1.0
proton_Kr_ioniz.ndt_supercycle = 1
EOF


### for 120k
max_steps = 120000
diag_period = 5000 or 10000
reduced_diag_period = 100

python plasma_column_mcc_picmi_v7.py \
    --write_inputs \
    --output_dir runs/cxx_H2_mcc_120k_physical \
    --inputs_name inputs_cxx_H2_mcc_120k_physical \
    --warpx_data_dir /home/cspark/Work/simulation_codes-working/warpx-data \
    --gas H2 \
    --neutralization 0.0 \
    --pressure_torr 1e-5 \
    --mcc none \
    --max_steps 120000 \
    --diag_period 10000 \
    --reduced_diag_period 100 \
    --reduced_diag_dir reducedfiles/ \
    --nx 24 --ny 24 --nz 128


cat >> runs/cxx_H2_mcc_120k_physical/inputs_cxx_H2_mcc_120k_physical <<'EOF'

collisions.collision_names = proton_H2_ioniz

proton_H2_ioniz.type = background_mcc
proton_H2_ioniz.species = beam_protons
proton_H2_ioniz.background_density = 3.2188332685e17
proton_H2_ioniz.max_background_density = 3.2188332685e17
proton_H2_ioniz.background_temperature = 300.0
proton_H2_ioniz.background_mass = 3.347e-27

proton_H2_ioniz.scattering_processes = ion_impact_ionization
proton_H2_ioniz.ion_impact_ionization_cross_section = /home/cspark/Work/simulation_codes-working/warpx-data/MCC_cross_sections/H2/proton_impact_ionization.dat
proton_H2_ioniz.ion_impact_ionization_energy = 0.0
proton_H2_ioniz.ion_impact_ionization_electron_species = plasma_electrons
proton_H2_ioniz.ion_impact_ionization_ion_species = gas_ions
proton_H2_ioniz.ion_impact_ionization_electron_energy = 1.0
proton_H2_ioniz.ndt_supercycle = 1
EOF



python plasma_column_mcc_picmi_v7.py \
    --write_inputs \
    --output_dir runs/cxx_Kr_mcc_120k_physical \
    --inputs_name inputs_cxx_Kr_mcc_120k_physical \
    --warpx_data_dir /home/cspark/Work/simulation_codes-working/warpx-data \
    --gas Kr \
    --neutralization 0.0 \
    --pressure_torr 1e-5 \
    --mcc none \
    --max_steps 120000 \
    --diag_period 10000 \
    --reduced_diag_period 100 \
    --reduced_diag_dir reducedfiles/ \
    --nx 24 --ny 24 --nz 128

cat >> runs/cxx_Kr_mcc_120k_physical/inputs_cxx_Kr_mcc_120k_physical <<'EOF'

collisions.collision_names = proton_Kr_ioniz

proton_Kr_ioniz.type = background_mcc
proton_Kr_ioniz.species = beam_protons

# 1e-5 torr at 300 K.
proton_Kr_ioniz.background_density = 3.2188332685e17
proton_Kr_ioniz.max_background_density = 3.2188332685e17
proton_Kr_ioniz.background_temperature = 300.0
proton_Kr_ioniz.background_mass = 1.391e-25

proton_Kr_ioniz.scattering_processes = ion_impact_ionization
proton_Kr_ioniz.ion_impact_ionization_cross_section = /home/cspark/Work/simulation_codes-working/warpx-data/MCC_cross_sections/Kr/proton_impact_ionization.dat
proton_Kr_ioniz.ion_impact_ionization_energy = 0.0

proton_Kr_ioniz.ion_impact_ionization_electron_species = plasma_electrons
proton_Kr_ioniz.ion_impact_ionization_ion_species = kr_ions

proton_Kr_ioniz.ion_impact_ionization_electron_energy = 1.0
proton_Kr_ioniz.ndt_supercycle = 1
EOF
