# app/core/permissions.py

from fastapi import Depends, HTTPException, status

from app.core.dependencies import get_current_user


class Role:
    SUPER_ADMIN = "SUPER_ADMIN"
    BRANCH_ADMIN = "BRANCH_ADMIN"
    STAFF = "STAFF"
    TECHNICIAN = "TECHNICIAN"
    CUSTOMER = "CUSTOMER"


def require_roles(*allowed_roles):
    def role_checker(
        current_user: dict = Depends(get_current_user),
    ):
        user_role = current_user.get("role")

        if user_role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to perform this action",
            )

        return current_user

    return role_checker


# Ready-to-use dependencies

RequireSuperAdmin = require_roles(
    Role.SUPER_ADMIN
)

RequireBranchAdmin = require_roles(
    Role.SUPER_ADMIN,
    Role.BRANCH_ADMIN
)

RequireStaff = require_roles(
    Role.SUPER_ADMIN,
    Role.BRANCH_ADMIN,
    Role.STAFF
)

RequireTechnician = require_roles(
    Role.SUPER_ADMIN,
    Role.BRANCH_ADMIN,
    Role.TECHNICIAN
)