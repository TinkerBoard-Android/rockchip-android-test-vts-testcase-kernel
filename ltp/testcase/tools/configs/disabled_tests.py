# Tests disabled
DISABLED_TESTS = [
    'cap_bounds.Cap_bounds',
    'commands.file01', # b/71414136
    # b/122327977 cgroup tests that either don't pass or take too long to run
    # e.g. stress tests
    'controllers.cgroup',
    'controllers.cgroup_fj_function_cpu',
    'controllers.cgroup_fj_function_cpuacct',
    'controllers.cgroup_fj_function_cpuset',
    'controllers.cgroup_fj_function_freezer',
    'controllers.cgroup_fj_stress_blkio_10_3_each',
    'controllers.cgroup_fj_stress_blkio_10_3_none',
    'controllers.cgroup_fj_stress_blkio_10_3_one',
    'controllers.cgroup_fj_stress_blkio_1_200_each',
    'controllers.cgroup_fj_stress_blkio_1_200_none',
    'controllers.cgroup_fj_stress_blkio_1_200_one',
    'controllers.cgroup_fj_stress_blkio_200_1_each',
    'controllers.cgroup_fj_stress_blkio_200_1_none',
    'controllers.cgroup_fj_stress_blkio_200_1_one',
    'controllers.cgroup_fj_stress_blkio_2_9_each',
    'controllers.cgroup_fj_stress_blkio_2_9_none',
    'controllers.cgroup_fj_stress_blkio_2_9_one',
    'controllers.cgroup_fj_stress_blkio_3_3_each',
    'controllers.cgroup_fj_stress_blkio_3_3_none',
    'controllers.cgroup_fj_stress_blkio_3_3_one',
    'controllers.cgroup_fj_stress_blkio_4_4_each',
    'controllers.cgroup_fj_stress_blkio_4_4_none',
    'controllers.cgroup_fj_stress_blkio_4_4_one',
    'controllers.cgroup_fj_stress_cpu_10_3_each',
    'controllers.cgroup_fj_stress_cpu_10_3_none',
    'controllers.cgroup_fj_stress_cpu_10_3_one',
    'controllers.cgroup_fj_stress_cpu_1_200_each',
    'controllers.cgroup_fj_stress_cpu_1_200_none',
    'controllers.cgroup_fj_stress_cpu_1_200_one',
    'controllers.cgroup_fj_stress_cpu_200_1_each',
    'controllers.cgroup_fj_stress_cpu_200_1_none',
    'controllers.cgroup_fj_stress_cpu_200_1_one',
    'controllers.cgroup_fj_stress_cpu_2_9_each',
    'controllers.cgroup_fj_stress_cpu_2_9_none',
    'controllers.cgroup_fj_stress_cpu_2_9_one',
    'controllers.cgroup_fj_stress_cpu_3_3_each',
    'controllers.cgroup_fj_stress_cpu_3_3_none',
    'controllers.cgroup_fj_stress_cpu_3_3_one',
    'controllers.cgroup_fj_stress_cpu_4_4_each',
    'controllers.cgroup_fj_stress_cpu_4_4_none',
    'controllers.cgroup_fj_stress_cpu_4_4_one',
    'controllers.cgroup_fj_stress_cpuacct_10_3_each',
    'controllers.cgroup_fj_stress_cpuacct_10_3_none',
    'controllers.cgroup_fj_stress_cpuacct_10_3_one',
    'controllers.cgroup_fj_stress_cpuacct_1_200_each',
    'controllers.cgroup_fj_stress_cpuacct_1_200_none',
    'controllers.cgroup_fj_stress_cpuacct_1_200_one',
    'controllers.cgroup_fj_stress_cpuacct_200_1_each',
    'controllers.cgroup_fj_stress_cpuacct_200_1_none',
    'controllers.cgroup_fj_stress_cpuacct_200_1_one',
    'controllers.cgroup_fj_stress_cpuacct_2_9_each',
    'controllers.cgroup_fj_stress_cpuacct_2_9_none',
    'controllers.cgroup_fj_stress_cpuacct_2_9_one',
    'controllers.cgroup_fj_stress_cpuacct_3_3_each',
    'controllers.cgroup_fj_stress_cpuacct_3_3_none',
    'controllers.cgroup_fj_stress_cpuacct_3_3_one',
    'controllers.cgroup_fj_stress_cpuacct_4_4_each',
    'controllers.cgroup_fj_stress_cpuacct_4_4_none',
    'controllers.cgroup_fj_stress_cpuacct_4_4_one',
    'controllers.cgroup_fj_stress_cpuset_10_3_each',
    'controllers.cgroup_fj_stress_cpuset_10_3_none',
    'controllers.cgroup_fj_stress_cpuset_10_3_one',
    'controllers.cgroup_fj_stress_cpuset_1_200_each',
    'controllers.cgroup_fj_stress_cpuset_1_200_none',
    'controllers.cgroup_fj_stress_cpuset_1_200_one',
    'controllers.cgroup_fj_stress_cpuset_200_1_each',
    'controllers.cgroup_fj_stress_cpuset_200_1_none',
    'controllers.cgroup_fj_stress_cpuset_200_1_one',
    'controllers.cgroup_fj_stress_cpuset_2_9_each',
    'controllers.cgroup_fj_stress_cpuset_2_9_none',
    'controllers.cgroup_fj_stress_cpuset_2_9_one',
    'controllers.cgroup_fj_stress_cpuset_3_3_each',
    'controllers.cgroup_fj_stress_cpuset_3_3_none',
    'controllers.cgroup_fj_stress_cpuset_3_3_one',
    'controllers.cgroup_fj_stress_cpuset_4_4_each',
    'controllers.cgroup_fj_stress_cpuset_4_4_none',
    'controllers.cgroup_fj_stress_cpuset_4_4_one',
    'controllers.cgroup_fj_stress_debug_10_3_each',
    'controllers.cgroup_fj_stress_debug_10_3_none',
    'controllers.cgroup_fj_stress_debug_10_3_one',
    'controllers.cgroup_fj_stress_debug_1_200_each',
    'controllers.cgroup_fj_stress_debug_1_200_none',
    'controllers.cgroup_fj_stress_debug_1_200_one',
    'controllers.cgroup_fj_stress_debug_200_1_each',
    'controllers.cgroup_fj_stress_debug_200_1_none',
    'controllers.cgroup_fj_stress_debug_200_1_one',
    'controllers.cgroup_fj_stress_debug_2_9_each',
    'controllers.cgroup_fj_stress_debug_2_9_none',
    'controllers.cgroup_fj_stress_debug_2_9_one',
    'controllers.cgroup_fj_stress_debug_3_3_each',
    'controllers.cgroup_fj_stress_debug_3_3_none',
    'controllers.cgroup_fj_stress_debug_3_3_one',
    'controllers.cgroup_fj_stress_debug_4_4_each',
    'controllers.cgroup_fj_stress_debug_4_4_none',
    'controllers.cgroup_fj_stress_debug_4_4_one',
    'controllers.cgroup_fj_stress_devices_10_3_each',
    'controllers.cgroup_fj_stress_devices_10_3_none',
    'controllers.cgroup_fj_stress_devices_10_3_one',
    'controllers.cgroup_fj_stress_devices_1_200_each',
    'controllers.cgroup_fj_stress_devices_1_200_none',
    'controllers.cgroup_fj_stress_devices_1_200_one',
    'controllers.cgroup_fj_stress_devices_200_1_each',
    'controllers.cgroup_fj_stress_devices_200_1_none',
    'controllers.cgroup_fj_stress_devices_200_1_one',
    'controllers.cgroup_fj_stress_devices_2_9_each',
    'controllers.cgroup_fj_stress_devices_2_9_none',
    'controllers.cgroup_fj_stress_devices_2_9_one',
    'controllers.cgroup_fj_stress_devices_3_3_each',
    'controllers.cgroup_fj_stress_devices_3_3_none',
    'controllers.cgroup_fj_stress_devices_3_3_one',
    'controllers.cgroup_fj_stress_devices_4_4_each',
    'controllers.cgroup_fj_stress_devices_4_4_none',
    'controllers.cgroup_fj_stress_devices_4_4_one',
    'controllers.cgroup_fj_stress_freezer_10_3_each',
    'controllers.cgroup_fj_stress_freezer_10_3_none',
    'controllers.cgroup_fj_stress_freezer_10_3_one',
    'controllers.cgroup_fj_stress_freezer_1_200_each',
    'controllers.cgroup_fj_stress_freezer_1_200_none',
    'controllers.cgroup_fj_stress_freezer_1_200_one',
    'controllers.cgroup_fj_stress_freezer_200_1_each',
    'controllers.cgroup_fj_stress_freezer_200_1_none',
    'controllers.cgroup_fj_stress_freezer_200_1_one',
    'controllers.cgroup_fj_stress_freezer_2_9_each',
    'controllers.cgroup_fj_stress_freezer_2_9_none',
    'controllers.cgroup_fj_stress_freezer_2_9_one',
    'controllers.cgroup_fj_stress_freezer_3_3_each',
    'controllers.cgroup_fj_stress_freezer_3_3_none',
    'controllers.cgroup_fj_stress_freezer_3_3_one',
    'controllers.cgroup_fj_stress_freezer_4_4_each',
    'controllers.cgroup_fj_stress_freezer_4_4_none',
    'controllers.cgroup_fj_stress_freezer_4_4_one',
    'controllers.cgroup_fj_stress_hugetlb_10_3_each',
    'controllers.cgroup_fj_stress_hugetlb_10_3_none',
    'controllers.cgroup_fj_stress_hugetlb_10_3_one',
    'controllers.cgroup_fj_stress_hugetlb_1_200_each',
    'controllers.cgroup_fj_stress_hugetlb_1_200_none',
    'controllers.cgroup_fj_stress_hugetlb_1_200_one',
    'controllers.cgroup_fj_stress_hugetlb_200_1_each',
    'controllers.cgroup_fj_stress_hugetlb_200_1_none',
    'controllers.cgroup_fj_stress_hugetlb_200_1_one',
    'controllers.cgroup_fj_stress_hugetlb_2_9_each',
    'controllers.cgroup_fj_stress_hugetlb_2_9_none',
    'controllers.cgroup_fj_stress_hugetlb_2_9_one',
    'controllers.cgroup_fj_stress_hugetlb_3_3_each',
    'controllers.cgroup_fj_stress_hugetlb_3_3_none',
    'controllers.cgroup_fj_stress_hugetlb_3_3_one',
    'controllers.cgroup_fj_stress_hugetlb_4_4_each',
    'controllers.cgroup_fj_stress_hugetlb_4_4_none',
    'controllers.cgroup_fj_stress_hugetlb_4_4_one',
    'controllers.cgroup_fj_stress_memory_10_3_each',
    'controllers.cgroup_fj_stress_memory_10_3_none',
    'controllers.cgroup_fj_stress_memory_10_3_one',
    'controllers.cgroup_fj_stress_memory_1_200_each',
    'controllers.cgroup_fj_stress_memory_1_200_none',
    'controllers.cgroup_fj_stress_memory_1_200_one',
    'controllers.cgroup_fj_stress_memory_200_1_each',
    'controllers.cgroup_fj_stress_memory_200_1_none',
    'controllers.cgroup_fj_stress_memory_200_1_one',
    'controllers.cgroup_fj_stress_memory_2_9_each',
    'controllers.cgroup_fj_stress_memory_2_9_none',
    'controllers.cgroup_fj_stress_memory_2_9_one',
    'controllers.cgroup_fj_stress_memory_3_3_each',
    'controllers.cgroup_fj_stress_memory_3_3_none',
    'controllers.cgroup_fj_stress_memory_3_3_one',
    'controllers.cgroup_fj_stress_memory_4_4_each',
    'controllers.cgroup_fj_stress_memory_4_4_none',
    'controllers.cgroup_fj_stress_memory_4_4_one',
    'controllers.cgroup_fj_stress_net_cls_10_3_each',
    'controllers.cgroup_fj_stress_net_cls_10_3_none',
    'controllers.cgroup_fj_stress_net_cls_10_3_one',
    'controllers.cgroup_fj_stress_net_cls_1_200_each',
    'controllers.cgroup_fj_stress_net_cls_1_200_none',
    'controllers.cgroup_fj_stress_net_cls_1_200_one',
    'controllers.cgroup_fj_stress_net_cls_200_1_each',
    'controllers.cgroup_fj_stress_net_cls_200_1_none',
    'controllers.cgroup_fj_stress_net_cls_200_1_one',
    'controllers.cgroup_fj_stress_net_cls_2_9_each',
    'controllers.cgroup_fj_stress_net_cls_2_9_none',
    'controllers.cgroup_fj_stress_net_cls_2_9_one',
    'controllers.cgroup_fj_stress_net_cls_3_3_each',
    'controllers.cgroup_fj_stress_net_cls_3_3_none',
    'controllers.cgroup_fj_stress_net_cls_3_3_one',
    'controllers.cgroup_fj_stress_net_cls_4_4_each',
    'controllers.cgroup_fj_stress_net_cls_4_4_none',
    'controllers.cgroup_fj_stress_net_cls_4_4_one',
    'controllers.cgroup_fj_stress_net_prio_10_3_each',
    'controllers.cgroup_fj_stress_net_prio_10_3_none',
    'controllers.cgroup_fj_stress_net_prio_10_3_one',
    'controllers.cgroup_fj_stress_net_prio_1_200_each',
    'controllers.cgroup_fj_stress_net_prio_1_200_none',
    'controllers.cgroup_fj_stress_net_prio_1_200_one',
    'controllers.cgroup_fj_stress_net_prio_200_1_each',
    'controllers.cgroup_fj_stress_net_prio_200_1_none',
    'controllers.cgroup_fj_stress_net_prio_200_1_one',
    'controllers.cgroup_fj_stress_net_prio_2_9_each',
    'controllers.cgroup_fj_stress_net_prio_2_9_none',
    'controllers.cgroup_fj_stress_net_prio_2_9_one',
    'controllers.cgroup_fj_stress_net_prio_3_3_each',
    'controllers.cgroup_fj_stress_net_prio_3_3_none',
    'controllers.cgroup_fj_stress_net_prio_3_3_one',
    'controllers.cgroup_fj_stress_net_prio_4_4_each',
    'controllers.cgroup_fj_stress_net_prio_4_4_none',
    'controllers.cgroup_fj_stress_net_prio_4_4_one',
    'controllers.cgroup_fj_stress_perf_event_10_3_each',
    'controllers.cgroup_fj_stress_perf_event_10_3_none',
    'controllers.cgroup_fj_stress_perf_event_10_3_one',
    'controllers.cgroup_fj_stress_perf_event_1_200_each',
    'controllers.cgroup_fj_stress_perf_event_1_200_none',
    'controllers.cgroup_fj_stress_perf_event_1_200_one',
    'controllers.cgroup_fj_stress_perf_event_200_1_each',
    'controllers.cgroup_fj_stress_perf_event_200_1_none',
    'controllers.cgroup_fj_stress_perf_event_200_1_one',
    'controllers.cgroup_fj_stress_perf_event_2_9_each',
    'controllers.cgroup_fj_stress_perf_event_2_9_none',
    'controllers.cgroup_fj_stress_perf_event_2_9_one',
    'controllers.cgroup_fj_stress_perf_event_3_3_each',
    'controllers.cgroup_fj_stress_perf_event_3_3_none',
    'controllers.cgroup_fj_stress_perf_event_3_3_one',
    'controllers.cgroup_fj_stress_perf_event_4_4_each',
    'controllers.cgroup_fj_stress_perf_event_4_4_none',
    'controllers.cgroup_fj_stress_perf_event_4_4_one',
    'controllers.cgroup_xattr',
    'controllers.cpuacct_100_1',
    'controllers.cpuacct_100_100',
    'controllers.cpuacct_10_10',
    'controllers.cpuacct_1_10',
    'controllers.cpuacct_1_100',
    'controllers.cpuset_hotplug',
    'controllers.cpuset_inherit',
    'controllers.cpuset_regression_test',
    'controllers.memcg_failcnt',
    'controllers.memcg_force_empty',
    'controllers.memcg_limit_in_bytes',
    'controllers.memcg_max_usage_in_bytes',
    'controllers.memcg_memsw_limit_in_bytes',
    'controllers.memcg_move_charge_at_immigrate',
    'controllers.memcg_stat',
    'controllers.memcg_stat_rss',
    'controllers.memcg_stress',
    'controllers.memcg_subgroup_charge',
    'controllers.memcg_usage_in_bytes',
    'controllers.memcg_use_hierarchy',
    'cpuhotplug.cpuhotplug02', # b/31154962
    'cpuhotplug.cpuhotplug03',
    'cpuhotplug.cpuhotplug04', # b/30688056
    'cpuhotplug.cpuhotplug06',
    'cve.cve-2014-0196', # b/112350736
    'cve.cve-2015-0235', # b/112350398
    'cve.cve-2016-4470', # b/112354289
    'cve.cve-2017-1000364', # b/112350736
    'cve.cve-2017-5669', # b/112354289
    'cve.cve-2017-5754', # b/123862031
    'dio.dio04',
    'dio.dio10',
    'dio.dio29', # takes too long
    'dio.dio30', # takes too long
    'dma_thread_diotest.dma_thread_diotest1', # b/32100169
    'dma_thread_diotest.dma_thread_diotest2',
    'dma_thread_diotest.dma_thread_diotest3',
    'dma_thread_diotest.dma_thread_diotest4',
    'dma_thread_diotest.dma_thread_diotest5',
    'dma_thread_diotest.dma_thread_diotest6',
    'dma_thread_diotest.dma_thread_diotest7',
    'fcntl-locktests_android.FCNTL_LOCKTESTS',
    'filecaps.Filecaps',
    'fs.fs_racer_32bit', # b/71780005
    'fs.fs_racer_64bit', # b/71780005
    'fs.ftest01',
    'fs.ftest03',
    'fs.ftest04',
    'fs.ftest05',
    'fs.ftest07',
    'fs.ftest08',
    'fs.gf01',
    'fs.gf02',
    'fs.gf03',
    'fs.gf04',
    'fs.gf05',
    'fs.gf06',
    'fs.gf07',
    'fs.gf08',
    'fs.gf09',
    'fs.gf10',
    'fs.gf11',
    'fs.gf14',
    'fs.gf15',
    'fs.gf16',
    'fs.gf17',
    'fs.gf18',
    'fs.gf19',
    'fs.gf20',
    'fs.gf21',
    'fs.gf22',
    'fs.gf23',
    'fs.gf24',
    'fs.gf25',
    'fs.gf26',
    'fs.gf27',
    'fs.gf28',
    'fs.gf29',
    'fs.gf30',
    'fs.inode02', # b/122260771
    'fs.iogen01',
    'fs.isofs',
    'fs.proc01', # b/71415362
    'fs.quota_remount_test01', # b/33008689
    'fs.rwtest01',
    'fs.rwtest02',
    'fs.rwtest03',
    'fs.rwtest04',
    'fs.rwtest05',
    'fs_bind.BindMounts',
    'fs_ext4.ext4-persist-prealloc',
    'fs_ext4.ext4-uninit-groups',
    'fsx.fsx-linux',
    'fsx.fsx-linux',
    'hugetlb.hugemmap05_1',
    'hugetlb.hugemmap05_2',
    'hugetlb.hugemmap05_3',
    'input.input01_64bit', # unstable 64-bits tests
    'input.input02_64bit',
    'input.input04_64bit',
    'input.input05_64bit',
    'input.input06_32bit',
    'input.input06_64bit',
    'kernel_misc.kmsg01', # b/32343072
    'kernel_misc.zram03',
    'mm.ksm01',
    'mm.ksm01_1', # b/71416672
    'mm.ksm03',
    'mm.ksm03_1',
    'mm.mallocstress01',
    'mm.max_map_count_32bit', # b/67981135
    'mm.max_map_count_64bit', # b/67981135
    'mm.min_free_kbytes',
    'mm.mmapstress10',
    'mm.mtest01',
    'mm.mtest01w', # b/30699880
    'mm.oom01_64bit', # b/31181781
    'mm.oom02_64bit',
    'mm.oom03_64bit',
    'mm.oom04_64bit',
    'mm.oom05_64bit',
    'mm.overcommit_memory01_64bit', # failing 64-bit only tests
    'mm.overcommit_memory02_64bit',
    'mm.overcommit_memory03_64bit',
    'mm.overcommit_memory04_64bit',
    'mm.overcommit_memory05_64bit',
    'mm.overcommit_memory06_64bit',
    'mm.shm_test01',
    'mm.swapping01_64bit',  # b/31181781
    'mm.thp01_32bit', # b/65636203
    'mm.thp01_64bit',
    'mm.thp02_64bit',
    'mm.thp03_64bit',
    'mm.vma01_64bit', # b/31181781
    'mm.vma03',
    'pipes.pipeio_1',
    'pipes.pipeio_3',
    'pipes.pipeio_4',
    'pipes.pipeio_5',
    'pipes.pipeio_6',
    'pipes.pipeio_8',
    'sched.sched_getattr01_32bit', # b/200686092
    'sched.sched_setattr01_32bit', # b/200686092
    'sched.trace_sched01',
    'syscalls.access04',
    'syscalls.alarm02', # b/112423802
    'syscalls.cve-2017-5669', # b/71416706
    'syscalls.fchown04',
    'syscalls.fchown04_16',
    'syscalls.fcntl14',
    'syscalls.fcntl14',
    'syscalls.fcntl14_64',
    'syscalls.fcntl17',
    'syscalls.fcntl17_64',
    'syscalls.fcntl35',
    'syscalls.fcntl35_64', # b/71416738
    'syscalls.fcntl36',
    'syscalls.fcntl36_64', # b/71416760
    'syscalls.fork13', # takes too long: ~45mins
    'syscalls.gethostbyname_r01',
    'syscalls.getrusage04', # b/32386191
    'syscalls.getxattr04', # b/65053723#comment20
    'syscalls.inotify03',
    'syscalls.ioctl03',
    'syscalls.ioctl04',
    'syscalls.ioctl06',
    'syscalls.kcmp03',
    'syscalls.kill12',
    'syscalls.lchown03',
    'syscalls.lchown03_16',
    'syscalls.lstat03',
    'syscalls.lstat03_64', # b/30688551
    'syscalls.mmap16',
    'syscalls.move_pages01', # move_pages syscalls requires userspace numa.
    'syscalls.move_pages02',
    'syscalls.move_pages03',
    'syscalls.move_pages04',
    'syscalls.move_pages05',
    'syscalls.move_pages06',
    'syscalls.move_pages07',
    'syscalls.move_pages08',
    'syscalls.move_pages09',
    'syscalls.move_pages10',
    'syscalls.move_pages11',
    'syscalls.move_pages12',
    'syscalls.nftw01',
    'syscalls.nftw6401',
    'syscalls.nice04',
    'syscalls.open08',
    'syscalls.open13', # https://android-review.googlesource.com/#/c/127908/
    'syscalls.perf_event_open02', # b/30675443
    'syscalls.prot_hsymlinks',
    'syscalls.pselect01', # b/65053723#comment19
    'syscalls.readdir02', # b/112422073
    'syscalls.rt_sigprocmask01_32bit', # b/31152672
    'syscalls.set_thread_area01_64bit', #b/112474139
    'syscalls.setpriority02', # b/73137289
    'syscalls.setregid02',
    'syscalls.setregid02_16',
    'syscalls.sigrelse01',
    'syscalls.splice02',
    'syscalls.utimensat01',
    'syscalls.vfork02',
    'tracing.dynamic_debug01', # b/71416822
    'tracing.ftrace_regression01', # b/69117476
]

# These tests fail under hwasan.
# mlock/mlockall tests activate lowmemorykiller and cause other unrelated tests to fail as well.
DISABLED_TESTS_HWASAN = [ # b/134613162
    'clone02',
    'clone03',
    'clone05',
    'clone06',
    'clone08',
    'clone09',
    'getcwd01',
    'mem01',
    'mlock01',
    'mlock03',
    'mlockall01',
    'mlockall02',
    'mlockall03',
    'munlock01',
    'sendmmsg01',
    'sigaltstack01',
    'time-schedule01',
]
