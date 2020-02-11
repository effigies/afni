from setuptools import setup

# Executable scripts obtained from the make target list_py_scripts
ENTRY_POINTS = {
    "console_scripts": [
        "1d_tool.py=afni_python.1d_tool.py:main",
        "1dplot.py=afni_python.1dplot.py:main",
        "djunct_calc_mont_dims.py=afni_python.djunct_calc_mont_dims.py:main",
        "djunct_combine_str.py=afni_python.djunct_combine_str.py:main",
        "djunct_select_str.py=afni_python.djunct_select_str.py:main",
        "DoPerRoi.py=afni_python.DoPerRoi.py:main",
        "abids_json_info.py=afni_python.abids_json_info.py:main",
        "abids_json_tool.py=afni_python.abids_json_tool.py:main",
        "abids_tool.py=afni_python.abids_tool.py:main",
        "afni_proc.py=afni_python.afni_proc.py:main",
        "afni_restproc.py=afni_python.afni_restproc.py:main",
        "afni_skeleton.py=afni_python.afni_skeleton.py:main",
        "afni_system_check.py=afni_python.afni_system_check.py:main",
        "afni_util.py=afni_python.afni_util.py:main",
        "align_epi_anat.py=afni_python.align_epi_anat.py:main",
        "apqc_make_html.py=afni_python.apqc_make_html.py:main",
        "apqc_make_tcsh.py=afni_python.apqc_make_tcsh.py:main",
        "auto_warp.py=afni_python.auto_warp.py:main",
        "BayesianGroupAna.py=afni_python.BayesianGroupAna.py:main",
        "demoExpt.py=afni_python.demoExpt.py:main",
        "eg_main_chrono.py=afni_python.eg_main_chrono.py:main",
        "fat_lat_csv.py=afni_python.fat_lat_csv.py:main",
        "fat_mat_sel.py=afni_python.fat_mat_sel.py:main",
        "fat_mvm_gridconv.py=afni_python.fat_mvm_gridconv.py:main",
        "fat_mvm_prep.py=afni_python.fat_mvm_prep.py:main",
        "fat_mvm_review.py=afni_python.fat_mvm_review.py:main",
        "fat_mvm_scripter.py=afni_python.fat_mvm_scripter.py:main",
        "fat_roi_row.py=afni_python.fat_roi_row.py:main",
        "gen_epi_review.py=afni_python.gen_epi_review.py:main",
        "gen_group_command.py=afni_python.gen_group_command.py:main",
        "gen_ss_review_scripts.py=afni_python.gen_ss_review_scripts.py:main",
        "gen_ss_review_table.py=afni_python.gen_ss_review_table.py:main",
        "lpc_align.py=afni_python.lpc_align.py:main",
        "make_pq_script.py=afni_python.make_pq_script.py:main",
        "make_random_timing.py=afni_python.make_random_timing.py:main",
        "make_stim_times.py=afni_python.make_stim_times.py:main",
        "meica.py=afni_python.meica.py:main",
        "neuro_deconvolve.py=afni_python.neuro_deconvolve.py:main",
        "parse_fs_lt_log.py=afni_python.parse_fs_lt_log.py:main",
        "python_module_test.py=afni_python.python_module_test.py:main",
        "quick.alpha.vals.py=afni_python.quick.alpha.vals.py:main",
        "read_matlab_files.py=afni_python.read_matlab_files.py:main",
        "realtime_receiver.py=afni_python.realtime_receiver.py:main",
        "RetroTS.py=afni_python.RetroTS.py:main",
        "slow_surf_clustsim.py=afni_python.slow_surf_clustsim.py:main",
        "tedana_wrapper.py=afni_python.tedana_wrapper.py:main",
        "timing_tool.py=afni_python.timing_tool.py:main",
        "uber_align_test.py=afni_python.uber_align_test.py:main",
        "uber_proc.py=afni_python.uber_proc.py:main",
        "uber_skel.py=afni_python.uber_skel.py:main",
        "uber_subject.py=afni_python.uber_subject.py:main",
        "uber_ttest.py=afni_python.uber_ttest.py:main",
        "unWarpEPI.py=afni_python.unWarpEPI.py:main",
        "xmat_tool.py=afni_python.xmat_tool.py:main",
    ]
}


if __name__ == '__main__':
    setup(
        name="afni_python",
        version="0.0.1",
        description="AFNI python package, contained in src/python_scripts of the AFNI codebase",
        url="git+https://github.com/afni/afni.git",
        author="AFNI team",
        author_email="afni.bootcamp@gmail.com",
        license="GPL3",
        packages=["afni_python"],
        install_requires=["numpy"],
        entry_points=ENTRY_POINTS,
        zip_safe=False,
    )
