#include <iostream>
#include <fstream> 
#include <vector>
#include <Eigen/Dense>

void parse_csv(std::string &infile, Eigen::MatrixXd &adjacency);
void build_hamil(Eigen::MatrixXd &adjacency, Eigen::MatrixXd &hamil, double alpha=-3, double beta=-2);
void diagonalize(Eigen::MatrixXd &hamil, Eigen::VectorXd &eigval, Eigen::MatrixXd &eigvec);
void output_csv(std::string &outfile, Eigen::VectorXd &eigval);

int main(int argc, char *argv[]) {
    std::string infile, outfile;
    try {
        if (argc != 3)
            throw std::exception();
        infile = argv[1];
        outfile = argv[2];
    }
    catch(...) {
        std::cout << "Please specify input xyz and output csv for adjacency" << std::endl;
        return 0;
    }
    
    Eigen::MatrixXd adjacency;
    parse_csv(infile, adjacency);
    std::cout << adjacency << std::endl;
    
    Eigen::MatrixXd hamil;
    build_hamil(adjacency, hamil);
    std::cout << hamil << std::endl;
    
    Eigen::VectorXd eigval;
    Eigen::MatrixXd eigvec;
    diagonalize(hamil, eigval, eigvec);
    std::cout << eigval << std::endl;

    output_csv(outfile, eigval);
}

void parse_csv(std::string &infile, Eigen::MatrixXd &adjacency) {
    std::ifstream csvstream (infile, std::ifstream::in);
    
    std::string line;
    std::vector<double> connectivity;
    while (std::getline(csvstream, line)) {
        std::stringstream ss(line);
        std::string val;
        while (std::getline(ss, val, ','))
            //connectivity.push_back(std::stoul(val));
            connectivity.push_back(std::stod(val));
    }

    int nrows = std::sqrt(connectivity.size());
    //Eigen::MatrixXd adj2 = Eigen::Map<Eigen::MatrixXd>(connectivity.data(), nrows, nrows);
    //std::cout << adj2 << std::endl;
    adjacency = Eigen::Map<Eigen::MatrixXd>(connectivity.data(), nrows, nrows);
}

void build_hamil(Eigen::MatrixXd &adjacency, Eigen::MatrixXd &hamil, double alpha, double beta) {
    hamil = Eigen::MatrixXd::Identity(adjacency.rows(), adjacency.cols()) * alpha;
    hamil += adjacency * beta;
}

void diagonalize(Eigen::MatrixXd &hamil, Eigen::VectorXd &eigval, Eigen::MatrixXd &eigvec) {
    Eigen::SelfAdjointEigenSolver<Eigen::MatrixXd> es(hamil);
    eigval = es.eigenvalues();
    eigvec = es.eigenvectors();
}

void output_csv(std::string &outfile, Eigen::VectorXd &eigval){
    std::ofstream outstream(outfile.c_str());
    const static Eigen::IOFormat CSVFormat(Eigen::StreamPrecision, Eigen::DontAlignCols, ", ", "\n");
    outstream << eigval.format(CSVFormat);
}

