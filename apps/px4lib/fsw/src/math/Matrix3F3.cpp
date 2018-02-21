#include <math/Matrix3F3.hpp>
#include <math.h>

using namespace math;


const Matrix3F3::RotLookup_t Matrix3F3::RotLookup[] = {
	{  0,   0,   0 },
	{  0,   0,  45 },
	{  0,   0,  90 },
	{  0,   0, 135 },
	{  0,   0, 180 },
	{  0,   0, 225 },
	{  0,   0, 270 },
	{  0,   0, 315 },
	{180,   0,   0 },
	{180,   0,  45 },
	{180,   0,  90 },
	{180,   0, 135 },
	{  0, 180,   0 },
	{180,   0, 225 },
	{180,   0, 270 },
	{180,   0, 315 },
	{ 90,   0,   0 },
	{ 90,   0,  45 },
	{ 90,   0,  90 },
	{ 90,   0, 135 },
	{270,   0,   0 },
	{270,   0,  45 },
	{270,   0,  90 },
	{270,   0, 135 },
	{  0,  90,   0 },
	{  0, 270,   0 },
	{270,   0, 270 },
	{180, 270,   0 },
	{  0,  90, 180 },
	{ 90,  90,   0 },
	{ 90,  68, 293 },
	{270,  90,   0 },
	{  0,   9, 180 },
};

Matrix3F3::Matrix3F3(Vector3F m0, Vector3F m1, Vector3F m2) :
	data{m0, m1, m2},
	nan{NAN,NAN,NAN}
{
};


Matrix3F3::Matrix3F3() :
	data{
		{0.0, 0.0, 0.0},
		{0.0, 0.0, 0.0},
		{0.0, 0.0, 0.0}
    },
    nan{NAN,NAN,NAN}
{
};


Matrix3F3::~Matrix3F3()
{
};


Vector3F& Matrix3F3::operator [] (uint32 i)
{
	if(i >= 3)
	{
		return nan;
	}
	else
	{
		return data[i];
	}
};


Vector3F Matrix3F3::operator [] (uint32 i) const
{
	if(i >= 3)
	{
		return nan;
	}
	else
	{
		return data[i];
	}
};


Matrix3F3 Matrix3F3::Transpose(void)
{
	Matrix3F3 res;

	res[0][0] = data[0][0];
	res[0][1] = data[1][0];
	res[0][2] = data[2][0];
	res[1][0] = data[0][1];
	res[1][1] = data[1][1];
	res[1][2] = data[2][1];
	res[2][0] = data[0][2];
	res[2][1] = data[1][2];
	res[2][2] = data[2][2];

	return res;
}


Matrix3F3 Matrix3F3::Identity() {
    Matrix3F3 matOut(
    		{1.0f, 0.0f, 0.0f},
    		{0.0f, 1.0f, 0.0f},
    		{0.0f, 0.0f, 1.0f}
			);

    return matOut;
}


void Matrix3F3::Zero(void)
{
	data[0][0] = 0.0f;
	data[0][1] = 0.0f;
	data[0][2] = 0.0f;
	data[1][0] = 0.0f;
	data[1][1] = 0.0f;
	data[1][2] = 0.0f;
	data[2][0] = 0.0f;
	data[2][1] = 0.0f;
	data[2][2] = 0.0f;
}


// overload * operator to provide a matrix product
Matrix3F3 Matrix3F3::operator*(const Matrix3F3 &matIn)
{
    Matrix3F3 matOut;

    matOut[0][0] = data[0][0]*matIn[0][0] + data[0][1]*matIn[1][0] + data[0][2]*matIn[2][0];
    matOut[0][1] = data[0][0]*matIn[0][1] + data[0][1]*matIn[1][1] + data[0][2]*matIn[2][1];
    matOut[0][2] = data[0][0]*matIn[0][2] + data[0][1]*matIn[1][2] + data[0][2]*matIn[2][2];

    matOut[1][0] = data[1][0]*matIn[0][0] + data[1][1]*matIn[1][0] + data[1][2]*matIn[2][0];
    matOut[1][1] = data[1][0]*matIn[0][1] + data[1][1]*matIn[1][1] + data[1][2]*matIn[2][1];
    matOut[1][2] = data[1][0]*matIn[0][2] + data[1][1]*matIn[1][2] + data[1][2]*matIn[2][2];

    matOut[2][0] = data[2][0]*matIn[0][0] + data[2][1]*matIn[1][0] + data[2][2]*matIn[2][0];
    matOut[2][1] = data[2][0]*matIn[0][1] + data[2][1]*matIn[1][1] + data[2][2]*matIn[2][1];
    matOut[2][2] = data[2][0]*matIn[0][2] + data[2][1]*matIn[1][2] + data[2][2]*matIn[2][2];

    return matOut;
}


// overload * operator to provide a matrix vector product
Vector3F Matrix3F3::operator*(const Vector3F &vecIn)
{
    Vector3F vecOut;
    vecOut[0] = data[0][0]*vecIn[0] + data[0][1]*vecIn[1] + data[0][2]*vecIn[2];
    vecOut[1] = data[1][0]*vecIn[0] + data[1][1]*vecIn[1] + data[1][2]*vecIn[2];
    vecOut[2] = data[2][0]*vecIn[0] + data[2][1]*vecIn[1] + data[2][2]*vecIn[2];
    return vecOut;
}


Matrix3F3 Matrix3F3::operator*(const float &scalar)
{
    Matrix3F3 matOut;

    matOut[0][0] = scalar*data[0][0];
    matOut[1][0] = scalar*data[1][0];
    matOut[2][0] = scalar*data[2][0];

    matOut[0][1] = scalar*data[0][1];
    matOut[1][1] = scalar*data[1][1];
    matOut[2][1] = scalar*data[2][1];

    matOut[0][2] = scalar*data[0][2];
    matOut[1][2] = scalar*data[1][2];
    matOut[2][2] = scalar*data[2][2];

    return matOut;
}


Matrix3F3 Matrix3F3::operator+(const Matrix3F3 &matIn) const
{
    Matrix3F3 matOut;

    matOut[0][0] = data[0][0] + matIn[0][0];
    matOut[1][0] = data[1][0] + matIn[1][0];
    matOut[2][0] = data[2][0] + matIn[2][0];

    matOut[0][1] = data[0][1] + matIn[0][1];
    matOut[1][1] = data[1][1] + matIn[1][1];
    matOut[2][1] = data[2][1] + matIn[2][1];

    matOut[0][2] = data[0][2] + matIn[0][2];
    matOut[1][2] = data[1][2] + matIn[1][2];
    matOut[2][2] = data[2][2] + matIn[2][2];

    return matOut;
}


Matrix3F3 Matrix3F3::RotationMatrix(Matrix3F3::Rotation_t boardRotation)
{
	Matrix3F3 matrix;

	float roll  = M_DEG_TO_RAD_F * (float)Matrix3F3::RotLookup[boardRotation].roll;
	float pitch = M_DEG_TO_RAD_F * (float)Matrix3F3::RotLookup[boardRotation].pitch;
	float yaw   = M_DEG_TO_RAD_F * (float)Matrix3F3::RotLookup[boardRotation].yaw;

	return Matrix3F3::FromEuler(roll, pitch, yaw);
}



Matrix3F3 Matrix3F3::FromEuler(float roll, float pitch, float yaw)
{
	Matrix3F3 matrix;

	float cp = cosf(pitch);
	float sp = sinf(pitch);
	float cr = cosf(roll);
	float sr = sinf(roll);
	float cy = cosf(yaw);
	float sy = sinf(yaw);

	matrix[0][0] = cp * cy;
	matrix[0][1] = (sr * sp * cy) - (cr * sy);
	matrix[0][2] = (cr * sp * cy) + (sr * sy);
	matrix[1][0] = cp * sy;
	matrix[1][1] = (sr * sp * sy) + (cr * cy);
	matrix[1][2] = (cr * sp * sy) - (sr * cy);
	matrix[2][0] = -sp;
	matrix[2][1] = sr * cp;
	matrix[2][2] = cr * cp;

	return matrix;
}



Vector3F Matrix3F3::ToEuler(void) const
{
	Vector3F euler;
	euler[1] = asinf(-data[2][0]);

	if (fabsf(euler[1] - M_PI_2) < 1.0e-3f) {
		euler[0] = 0.0f;
		euler[2] = atan2f(data[1][2] - data[0][1], data[0][2] + data[1][1]) + euler[0];

	} else if (fabsf(euler[1] + M_PI_2) < 1.0e-3f) {
		euler[0] = 0.0f;
		euler[2] = atan2f(data[1][2] - data[0][1], data[0][2] + data[1][1]) - euler[0];

	} else {
		euler[0] = atan2f(data[2][1], data[2][2]);
		euler[2] = atan2f(data[1][0], data[0][0]);
	}

	return euler;
}

void Matrix3F3::getCofactor(const Matrix3F3 &mat, Matrix3F3 &temp, int p, int q, int n)
{
    int i = 0, j = 0;

    // Looping for each element of the matrix
    for (int row = 0; row < n; row++)
    {
        for (int col = 0; col < n; col++)
        {
            //  Copying into temporary matrix only those element
            //  which are not in given row and column
            if (row != p && col != q)
            {
                temp[i][j++] = mat[row][col];
                // Row is filled, so increase row index and
                // reset col index
                if (j == n - 1)
                {
                    j = 0;
                    i++;
                }
            }
        }
    }
}



float Matrix3F3::DeterminantRecursive(const Matrix3F3 &mat, int n)
{
    if (n < 1)
    {
        return NAN;
    }

    float D = 0.0f; // Initialize result
 
    //  Base case : if matrix contains single element
    if (n == 1)
    {
        return mat[0][0];
    }

    Matrix3F3 temp; // To store cofactors
    temp.Zero();
 
    float sign = 1.0f;  // To store sign multiplier
 
     // Iterate for each element of first row
    for (int f = 0; f < n; f++)
    {
        // Getting Cofactor of mat[0][f]
        getCofactor(mat, temp, 0, f, n);
        D += sign * mat[0][f] * DeterminantRecursive(temp, n - 1);
 
        // terms are to be added with alternate sign
        sign = -sign;
    }
 
    return D;
}


float Matrix3F3::Determinant(void)
{
    return DeterminantRecursive(*this, SIZE);
}


Matrix3F3 Matrix3F3::Inversed(void)
{
    Matrix3F3 matOut;
    matOut.Zero();
    Matrix3F3 temp;
    temp.Zero();
    int i,j = 0;
    float determinant = 0;

    determinant = Determinant();

    if (0.0f == determinant || !isfinite(determinant))
    {
        return Matrix3F3(nan, nan, nan);
    }

    for(j = 0; j < SIZE; j++)
    {
        for(i = 0; i < SIZE; i++)
        {
            getCofactor(*this, temp, j, i, SIZE);
            matOut[i][j] = DeterminantRecursive(temp, SIZE - 1) / determinant;
            if (1 == (i+j)%2)
            {
                matOut[i][j] = -matOut[i][j];
            }

        }
    }
    
    return matOut;
}
