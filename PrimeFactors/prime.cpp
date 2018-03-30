/* prime.cpp
 * Author: Cody Lewis
 * Date: 1/07/2017
 * Description:
 * a program that finds the prime numbers up to a bound
 */
#include<iostream>
#include<vector>
int findPrime(int bound){
	//Description: finds and prints prime numbers up to a set bound
	//Pre-conditions: a bound must be sent in
	//Post-conditions: the prime numbers up to the bound are printed
	bool prime;
  std::vector<int> primeVector = {2};
	for(int counter=3; counter<bound; counter++){
		prime = true;
    for(int i = 0; i < primeVector.size(); i++){
      if(counter%primeVector[i] == 0){
        prime = false;
        break;
      }
    }
		if(prime){
      primeVector.push_back(counter);
		}
	}
  std::cout << "The primes up to " << bound << " are ";
  for(int i = 0; i < primeVector.size(); i++){
    std::cout << primeVector[i] << ", ";
  }
  std::cout << std::endl;
	return 1;
}
int main(){
	try{
		int bound;
    std::cout << "This program finds the prime numbers up to the bound you will input: ";
    std::cin >> bound;
		if(bound<2){
			throw 1;
		}
		findPrime(bound);
	} catch(int params) {
		switch(params){
      case 1: std::cout << "The number you entered cannot be calculated as prime" << std::endl;
		}
	}
	return 0;
}
