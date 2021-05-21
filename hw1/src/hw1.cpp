// include ros library
#include "ros/ros.h"

// include msg library
#include <geometry_msgs/Twist.h>

// include cpp library 
#include <cstdio>
#include <unistd.h>
#include <termios.h>
#include <fcntl.h>
geometry_msgs::Twist vel_msg;

char getch()
{		
  	int flags = fcntl(0, F_GETFL, 0);
  	fcntl(0, F_SETFL, flags | O_NONBLOCK);
	
  	char buf = 0;
  	struct termios old = {0};
  	if (tcgetattr(0, &old) < 0) {
      	perror("tcsetattr()");
  	}
  	old.c_lflag &= ~ICANON;
  	old.c_lflag &= ~ECHO;
  	old.c_cc[VMIN] = 1;
  	old.c_cc[VTIME] = 0;
  	if (tcsetattr(0, TCSANOW, &old) < 0) {
      	perror("tcsetattr ICANON");
 	}
  	if (read(0, &buf, 1) < 0) {
      	//perror ("read()");
  	}
  	old.c_lflag |= ICANON;
  	old.c_lflag |= ECHO;
  	if (tcsetattr(0, TCSADRAIN, &old) < 0) {
      	perror ("tcsetattr ~ICANON");
  	}
  	return (buf);
}

void KeyboardControl()
{
  	int c = getch();
  	if (c != EOF)
  	{
		std::cout<< "c variable"<< c <<std::endl;
		/*Please input your codes here*/
		switch(c)
    	{
      		case 87://W
        		vel_msg.linear.x += 0.1;
        		break;
      		case 83://S       
        		vel_msg.linear.x -= 0.1;
        		break;
      		case 65://A
        		vel_msg.angular.z += 0.1;
        		break;
      		case 68://D
        		vel_msg.angular.z -= 0.1;
        		break;
        	case 73://I
        		vel_msg.linear.x = 0.0;
        		vel_msg.angular.z = 0.0;
        		break;
    	}
  	}
}

int main(int argc, char **argv)
{
  	ros::init(argc, argv, "tutorial_1");
  	ros::NodeHandle n;

  	// declare publisher
  	ros::Publisher turtlesim_pub = n.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 100);

  	// setting frequency as 100 Hz
  	ros::Rate loop_rate(100);

  	printf("KeyboardControl start\n");

  	int count = 0;
  	while (ros::ok()){
    	KeyboardControl();

    	turtlesim_pub.publish(vel_msg);
		std::cout<<"count :"<< ros::Time::now() <<std::endl;
		std::cout<<"linear :"<< ros::Time::now() <<std::endl;
		std::cout<<"angular :"<< ros::Time::now() <<std::endl;

    	count ++;
    	ros::spinOnce();
    	loop_rate.sleep();
  	}
  	return 0;
}



