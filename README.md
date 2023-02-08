# Update

### Set Python virtual environment

```
> cd 'folder of ai-pilot-project'
> python -m venv .venv
> .venv\Scripts\activate.bat
(.venv) > python.exe -m pip install --upgrade pip
(.venv) > pip install -r requirements.txt
(.venv) > DO SOMETHING...
```

### Installed libraries

```
pip install jsbsim
pip install matplotlib
pip install tensorflow==2.5.0
```

### jsbsim 코드 복제

```
cd src\environments
git clone https://github.com/JSBSim-Team/jsbsim.git
```
> jsbsim 리파지토리 전체 정보가 필요하지는 않을 듯...
> ``aircraft``, ``data_output``, ``engine`` 정도만 유지해도 될 듯...

### CUDA Toolkit 11.0 설치

* https://developer.nvidia.com/cuda-11.0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exenetwork
* 참고
  * https://github.com/tensorflow/tensorflow/issues/49295
* PC를 재시작한다!

### 코드 수정

* src\environments\jsbsim\JSBSimEnv.py, 34번 라인

  ```python
  # self.fdm = jsbsim.FGFDMExec('./src/environments/jsbsim/jsbsim/', None)   # declaring the sim and setting the path
  self.fdm = jsbsim.FGFDMExec('C:/JSBSim/', None) 
  ```

* QPlane.py, 54-55번 라인

  ```python
  # jsbRender = False  # will send UDP data to flight gear for rendering if True
  # jsbRealTime = False  # will slow down the physics to portrait real time rendering
  jsbRender = True  
  jsbRealTime = True  
  ```

### c172r aircraft downlaod
* https://sourceforge.net/p/flightgear/fgaddon/HEAD/tree/trunk/Aircraft/c172r/
* 저장할 위치 : C:\Program Files\FlightGear 2020.3\data\Aircraft

### jsbsim data_out 설정

* jsbsim 리파지토리에서 data_output/flightgear.xml 파일을 아래 구조처럼 복사한다.
  ```
  ├─src
  │  ├─environments
  │  │  ├─jsbsim
  │  │  │  ├─data_output
  │  │  │  │  ├─flightgear.xml
  ```

### 실행

* Flightgear 실행
  ```
  fgfs.exe --fdm=null --native-fdm=socket,in,60,localhost,5550,udp --aircraft=c172r --airport=RKJJ
  ```

* QPlane 실행
  ```
  python Qplane.py
  ```

  > UDP 통신을 하므로, Flightgear와 QPlane 간의 실행 순서는 상관 없음.

---
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/JDatPNW/QPlane">
    <img src="misc/QPlaneLogo.svg" alt="Logo" width="80%">
  </a>

  <h3 align="center">QPlane</h3>

  <p align="center">
    Fixed Wing Flight Simulation Environment for Reinforcement Learning
    <br />
    <br />
    <a href="https://github.com/JDatPNW/QPlane/issues">Report Bug</a>
    ·
    <a href="https://github.com/JDatPNW/QPlane/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This repository is being written as part of my masters thesis. I am trying to develop a fixed wing attitude control system using Reinforcement Learning algorithms. As of right now this code works with XPlane 11 and QLearning as well as Deep QLearning.

### Built With

This project is built with these frameworks, libraries, repositories and software:
* [tensorflow](https://www.tensorflow.org/)
* [XPlaneConnect](https://github.com/nasa/XPlaneConnect)
* [XPlane 11](https://www.x-plane.com/)
* [JSBSim](https://github.com/JSBSim-Team/jsbsim)
* [Flightgear](https://www.flightgear.org/)



<!-- GETTING STARTED -->
## Getting Started

Simple clone this repository to your local filesystem:
```sh
git clone https://github.com/JDatPNW/QPlane
```

### Prerequisites

Tested and running with:

|Software | Version|
|-----|-----|
|XPlane11 Version: | 11.50r3 (build 115033 64-bit, OpenGL)|
|JSBSim Version: | 1.1.5 (GitHub build 277)|
|Flightgear Version: | 2020.3.6|
|XPlaneConnect Version: | 1.3-rc.2|
|Python Version: | 3.8.2|
|numpy Version: | 1.19.4|
|tensorflow Version: | 2.3.0|
|Anaconda Version: | 4.9.2|
|Windows Version: | 1909|


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/JDatPNW/QPlane
   ```
2. Install the above listed software (other versions might work)
    * For JSBSim clone the JSBsim repo into `src/environments/jsbsim`
    * For visualizing JSBSim download the c172r plane model in the Flightgear Menu

<!-- USAGE EXAMPLES -->
## Usage

Once downloaded and installed, simply execute the `QPlane.py` file to run and test the code.
* For the XPlane Environment, XPlane (the game) needs to run.
* For JSBSim with rendering, Flightgear needs to run with the following flags `--fdm=null --native-fdm=socket,in,60,localhost,5550,udp --aircraft=c172r --airport=RKJJ`

<!-- Proof -->
## Proof
This gif shows an attitude agent (using Q-Learning) in action and compares it to the baseline random agent.

<p align="center">
    <img src="misc/proof.gif" alt="Logo" width="80%">
</p>

[Full Video in HD](https://www.youtube.com/watch?v=Puq8paN3BKs)


<!-- ROADMAP -->
## Roadmap

Planned future features are:
* Double Deep Q Learning


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `misc/LICENSE` for more information.



<!-- CONTACT -->
## Contact

Github Pages: [JDatPNW](https://JDatPNW.github.io)

<!-- Publications -->
## Publications
* [ACM MMSys'21 - QPlane: An Open-Source Reinforcement Learning Toolkit for Autonomous Fixed Wing Aircraft Simulation](https://dl.acm.org/doi/abs/10.1145/3458305.3478446)
  * [ACM MMSys'21 Presentation](https://youtu.be/F0RdZFW1EWw)

<!-- Citation -->
## Citation

Please cite `QPlane` if you use it in your research.
```tex
@inproceedings{richter2021qplane,
  title={QPlane: An Open-Source Reinforcement Learning Toolkit for Autonomous Fixed Wing Aircraft Simulation},
  author={Richter, David J and Calix, Ricardo A},
  booktitle={Proceedings of the 12th ACM Multimedia Systems Conference},
  pages={261--266},
  year={2021}
}
```
or

> Richter, D. J., & Calix, R. A. (2021, June). QPlane: An Open-Source Reinforcement Learning Toolkit for Autonomous Fixed Wing Aircraft Simulation. In Proceedings of the 12th ACM Multimedia Systems Conference (pp. 261-266).

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Readme Template](https://github.com/othneildrew/Best-README-Template)
* [Python Programming - DeepRL DQN](https://pythonprogramming.net/q-learning-reinforcement-learning-python-tutorial/)
* [Deeplizard - DeepRL DQN](https://deeplizard.com/learn/playlist/PLZbbT5o_s2xoWNVdDudn51XM8lOuZ_Njv)
* [NeuralNetAI - DDQN](https://www.neuralnet.ai/) (Video found on the linked YouTube, not on  the site)
* [Python Lessons - DeepRL PPO](https://pylessons.com/CartPole-reinforcement-learning/)
* [adderbyte](https://github.com/adderbyte/GYM_XPLANE_ML)
* [XPlane Forum](https://forums.x-plane.org/index.php?/forums/topic/236878-xplane11-xplaneconnect-question-about-resettingspawning-the-plane/&tab=comments#comment-2118006)
* [JSBSim](https://github.com/JSBSim-Team/jsbsim)
