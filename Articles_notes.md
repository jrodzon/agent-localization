# Article: EVOPS Benchmark: Evaluation of Plane Segmentation from RGBD and LiDAR Data
Link: <https://arxiv.org/pdf/2204.05799>

Comparison of available methods of plane segmentation.
What may be found there:
1) labeled RGBD and LiDAR data from popular SLAM/odometry datasets
2) pip package: https://pypi.org/project/evops
3) docker images of existing open-source plane segmentation approaches: https://github.com/MobileRoboticsSkoltech/3D-plane-segmentation
4) evaluation of 3D data approaches on RGBD
5) learnable baseline for plane segmentation in LiDAR: https://github.com/MobileRoboticsSkoltech/dsnet-plane-segmentation


# Article: Fast plane segmentation with line primitives for RGB-D sensor
Link: <https://www.researchgate.net/publication/312103071_Fast_plane_segmentation_with_line_primitives_for_RGB-D_sensor>

Brings up several methods for plane segmentation with their pros and cons, eg:
- RANSAC-like - tends to oversimplify complex planar structures
- Rabbani - region-growing-based approach using smoothness constraint (knn or fixed distance n)
- Holz and Behnke - extended Rabbani
- Salas-Moreno - similar approach using connected component labeling
- Guan - treat range image as a Markov random field and solve the association problem with graph-based global energy minimization
- Matsumoto - piece-wise plane fitting approach

Proposes it's own method of plane segmentation with 2-D scanlines.

# Article: PlaneNet: Piece-wise Planar Reconstruction from a Single RGB Image
Link: <https://art-programmer.github.io/planenet.html>
Github: <https://github.com/art-programmer/PlaneNet>

Proposes Deep Neural Network for reconstructing planes for RGB image.
Related works:
- piece-wise planar reconstruction - plane fitting
- Saxena - create depthmap from RGB with CNN (without plane detection)
- layout estimation - most approaches estimate vanishing points with heuristics and from these points infere deminant planes
- line analysis - statistical analysis of line directions (first attempts in 60s - Robert's system)

They use Detailed Residual Networks (DRNs)
Quite complex structure of neural networks - multiple modules with multiple layers.

This is an inferior version of PlaneRCNN. PlaneRCNN is better and was developed later by the same group.

# Article: PlaneSegNet: Fast and Robust Plane Estimation Using a Single-stage Instance Segmentation CNN
Link: <https://www.dfki.de/fileadmin/user_upload/import/11532_ICRA_2021___PlaneSegNet.pdf>


